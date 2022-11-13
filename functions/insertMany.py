import mysql.connector
from mysql.connector import Error


def insertMany(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Data berhasil masuk!")
    except Error as err:
        print(f"Error: '{err}'")
