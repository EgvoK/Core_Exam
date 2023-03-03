import sqlite3
import re

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

        for row in report:
            counter += 1
            for category in categories:
                category_id = category[0]
                if category_id == row[0]:
                    category_name = category[1]
            print(f"{counter}. {category_name} - {row[1]}$")

# SELECT
#    stud AS [Student],
#    First(idp) AS [id_prepod],
#    Max(cnt) AS [Counter]
# FROM T3
# GROUP BY T3.stud;





