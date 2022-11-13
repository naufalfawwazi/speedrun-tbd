import mysql.connector
from mysql.connector import Error
from termcolor import cprint


def delete(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.execute(sql, val)
        connection.commit()
        cprint("Data berhasil di hapus", 'green', 'on_green')
    except Error as err:
        print(f"Error: '{err}'")
