import sqlite3
import traceback
import sys


try:
    connection = sqlite3.connect('database.db')

    with open('schema.sql') as file:
        connection.executescript(file.read())

    cur = connection.cursor()
    print("Connection is successfully!")

    cur.execute("insert into categories(category_name) values ('Home')")
    cur.execute("insert into categories(category_name) values ('Health')")
    cur.execute("insert into categories(category_name) values ('Nutrition')")
    cur.execute("insert into categories(category_name) values ('Cloth')")
    cur.execute("insert into categories(category_name) values ('Shoes')")
    cur.execute("insert into categories(category_name) values ('Present')")
    cur.execute("insert into categories(category_name) values ('Services')")
    cur.execute("insert into categories(category_name) values ('Transport')")
    cur.execute("insert into categories(category_name) values ('Miscellaneous')")

    cur.execute("insert into expenditures (expenditure_name, expenditure_date, category_id) values (?, ?, ?)",
                ("Example", "2023-02-25", 9))

    print("Entries added successfully!")
    connection.commit()
    cur.close()

except sqlite3.Error as error:
    print("Failed to load data into table!")
    print("Exception class: ", error.__class__)
    print("Exception", error.args)
    print("Details: ")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))

finally:
    if connection:
        connection.close()
        print("Connection is closed!")



