import mysql.connector
from mysql.connector import Error
from termcolor import cprint


def insertMany(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        cprint("Data berhasil masuk", 'green', 'on_green')
    except Error as err:
        print(f"Error: '{err}'")
