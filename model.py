import sqlite3


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
            search_id = expenditure[3]

            for category in categories:
                category_id = category[0]
                if category_id == search_id:
                    category_name = category[1]

            print(f"{counter}. {expenditure_name} - {expenditure_date} - {category_name}")





