import mysql.connector
from mysql.connector import Error
from termcolor import cprint


def connection(host_name, username, password, dbName):
    connection: None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=username,
            passwd=password,
            database=dbName
        )
        print(cprint("Koneksi Database Berhasil", 'green', 'on_green'))
    except Error as err:
        print(f"Error: '{err}'")

    return connection
