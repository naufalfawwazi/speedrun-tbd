import mysql.connector
from termcolor import cprint


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        cprint(f"Error:  '{err}'", 'white', 'on_red')
