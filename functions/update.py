import mysql.connector
from mysql.connector import Error
from termcolor import cprint


def update(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.execute(sql, val)
        connection.commit()
        cprint("Data berhasil di update", 'green', 'on_green')
    except Error as err:
        cprint(f"Error: '{err}'", 'white', 'on_red')
