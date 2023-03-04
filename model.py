import sqlite3
import re
import csv

import config


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


class Model:

    @staticmethod
    def get_expenditures():
        counter = 0
        connection = get_db_connection()
        expenditures = connection.execute('select * from expenditures').fetchall()
        categories = connection.execute('select * from categories').fetchall()
        connection.close()

        for expenditure in expenditures:
            counter += 1
            expenditure_name = expenditure[1]
            expenditure_date = expenditure[2]
            amount = expenditure[3]
            search_id = expenditure[4]

            for category in categories:
                category_id = category[0]
                if category_id == search_id:
                    category_name = category[1]

            print(f"{counter}. {expenditure_name} - {expenditure_date} - {category_name} - {amount}$")

    @staticmethod
    def add_expenditure():
        connection = get_db_connection()
        categories = connection.execute('select * from categories').fetchall()

        while True:
            name = input("Enter cost name (max 100 symbols): ")
            if len(name) > 100:
                print("Enter correct name!")
            else:
                expenditure_name = name
                break

        while True:
            date = input("Enter cost date (YYYY-MM-DD): ")
            validator = re.compile(r"^2[0-9]{3}-[0-1][0-9]-[0-3][0-9]$")
            val_date = validator.match(date)
            if val_date is None:
                print("Enter correct date!")
            else:
                expenditure_date = date
                break
        while True:
            money = input("Enter cost amount: ")
            if money.isdigit():
                amount = money
                break
            else:
                print("Enter correct amount! ")

        while True:
            list_id = []
            for category in categories:
                category_id = category[0]
                category_name = category[1]
                list_id.append(category_id)
                print(f"{category_id} - {category_name}")
            c_id = int(input("Enter the category number from the list above: "))
            if c_id not in list_id:
                print("Enter correct category number!")
            else:
                category_id = c_id
                break

        connection.execute('insert into expenditures (expenditure_name, expenditure_date, amount, category_id) '
                           'values (?, ?, ?, ?)', (expenditure_name, expenditure_date, amount, category_id))
        connection.commit()
        connection.close()

    @staticmethod
    def get_group_by_category():
        counter = 0

        connection = get_db_connection()
        categories = connection.execute('select * from categories').fetchall()
        report = connection.execute('select * from expenditures group by category_id')

        print(f"{config.SEPARATOR}\nREPORT - GROUP BY CATEGORY:\n{config.SEPARATOR}")
        for row in report:
            counter += 1
            for category in categories:
                category_id = category[0]
                if category_id == row[4]:
                    category_name = category[1]

            print(f"{counter}. {category_name} - {row[3]}$")

    @staticmethod
    def get_group_by_name():
        counter = 0

        connection = get_db_connection()
        report = connection.execute('select * from expenditures group by expenditure_name')

        print(f"{config.SEPARATOR}\nREPORT - GROUP BY NAME:\n{config.SEPARATOR}")
        for row in report:
            counter += 1
            print(f"{counter}. {row[1]} - {row[3]}$")

    @staticmethod
    def get_group_by_date():
        counter = 0

        connection = get_db_connection()
        report = connection.execute('select * from expenditures group by expenditure_date')

        print(f"{config.SEPARATOR}\nREPORT - GROUP BY DATE:\n{config.SEPARATOR}")
        for row in report:
            counter += 1
            print(f"{counter}. {row[2]} - {row[3]}$")

    @staticmethod
    def get_max_in_categories():
        counter = 0

        connection = get_db_connection()
        categories = connection.execute('select * from categories').fetchall()
        report = connection.execute('select category_id, max(amount) from expenditures group by category_id')

        print(f"{config.SEPARATOR}\nREPORT - MAX IN EACH CATEGORIES:\n{config.SEPARATOR}")

        for row in report:
            counter += 1
            for category in categories:
                category_id = category[0]
                if category_id == row[0]:
                    category_name = category[1]
            print(f"{counter}. {category_name} - {row[1]}$")

    @staticmethod
    def get_min_in_categories():
        counter = 0

        connection = get_db_connection()
        categories = connection.execute('select * from categories').fetchall()
        report = connection.execute('select category_id, min(amount) from expenditures group by category_id')

        print(f"{config.SEPARATOR}\nREPORT - MIN IN EACH CATEGORIES:\n{config.SEPARATOR}")

        for row in report:
            counter += 1
            for category in categories:
                category_id = category[0]
                if category_id == row[0]:
                    category_name = category[1]
            print(f"{counter}. {category_name} - {row[1]}$")

    @staticmethod
    def get_max_in_period():
        connection = get_db_connection()

        while True:
            date = input("Enter cost date (YYYY-MM-DD): ")
            validator = re.compile(r"^2[0-9]{3}-[0-1][0-9]-[0-3][0-9]$")
            val_date = validator.match(date)
            if val_date is None:
                print("Enter correct date!")
            else:
                search_date = date
                break

        print(f"{config.SEPARATOR}\nREPORT - MAX IN THE PERIOD:\n{config.SEPARATOR}")

        valid_dates = []
        dates = connection.execute('select expenditure_date from expenditures group by expenditure_date')
        for item in dates:
            valid_dates.append(item[0])

        if search_date in valid_dates:
            report = connection.execute('''select expenditure_name, expenditure_date, max(amount) from expenditures 
                                    where expenditure_date=? group by expenditure_date''', (search_date,))

            for row in report:
                print(f"1. {row[0]} - {row[1]} - {row[2]}$")

        else:
            print(f"{config.SEPARATOR}\nCosts in {search_date} not found!")

    @staticmethod
    def get_min_in_period():
        valid_dates = []
        connection = get_db_connection()

        while True:
            date = input("Enter cost date (YYYY-MM-DD): ")
            validator = re.compile(r"^2[0-9]{3}-[0-1][0-9]-[0-3][0-9]$")
            val_date = validator.match(date)
            if val_date is None:
                print("Enter correct date!")
            else:
                search_date = date
                break

        print(f"{config.SEPARATOR}\nREPORT - MIN IN THE PERIOD:\n{config.SEPARATOR}")

        dates = connection.execute('select expenditure_date from expenditures group by expenditure_date')
        for item in dates:
            valid_dates.append(item[0])

        if search_date in valid_dates:
            report = connection.execute('''select expenditure_name, expenditure_date, min(amount) from expenditures 
                                    where expenditure_date=? group by expenditure_date''', (search_date,))

            for row in report:
                print(f"1. {row[0]} - {row[1]} - {row[2]}$")

        else:
            print(f"{config.SEPARATOR}\nCosts in {search_date} not found!")

    @staticmethod
    def export_to_csv():
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("select expenditure_name, expenditure_date, category_name, amount "
                       "from expenditures left join categories on categories.id = expenditures.category_id;")

        with open('export.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)
        connection.close()

    @staticmethod
    def import_from_csv():
        connection = get_db_connection()
        cursor = connection.cursor()

        with open('import.csv', 'r') as file:
            dr = csv.DictReader(file)
            data = [(i['name'], i['date'], i['category_id'], i['amount']) for i in dr]

        cursor.executemany('insert into expenditures (expenditure_name, expenditure_date, category_id, amount) '
                           'values (?, ?, ?, ?);', data)
        connection.commit()
        connection.close()

    @staticmethod
    def add_category():
        valid_categories = []
        connection = get_db_connection()
        categories = connection.execute('select * from categories').fetchall()

        while True:
            name = input("Enter category name: ")
            for category in categories:
                valid_categories.append(category[1])

            if name in valid_categories:
                print(f"{config.SEPARATOR}\nThis category already exists!\n{config.SEPARATOR}")
            else:
                connection.execute("insert into categories(category_name) values (?);", (name,))
                connection.commit()
                connection.close()
                break

    @staticmethod
    def del_category():
        not_empty_categories = []
        connection = get_db_connection()
        category_ids = connection.execute('select category_id from expenditures').fetchall()
        categories = connection.execute('select * from categories').fetchall()
        for item in category_ids:
            not_empty_categories.append(item[0])

        while True:
            list_id = []
            for category in categories:
                category_id = category[0]
                category_name = category[1]
                list_id.append(category_id)
                print(f"{category_id} - {category_name}")

            del_id = input("Enter the category number from the list above: ")
            if del_id in list_id:
                print("Selected category is not empty!")
            else:
                connection.execute("delete from categories where id = ?", (del_id,))
                connection.commit()
                connection.close()
                break










