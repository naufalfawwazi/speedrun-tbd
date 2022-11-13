import mysql.connector
from mysql.connector import Error


def connection(host_name, username, password):
    connection: None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=username,
            passwd=password
        )
        print("Koneksi Berhasil")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


connection("localhost", "root", "root")
