import sqlite3
import re


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





