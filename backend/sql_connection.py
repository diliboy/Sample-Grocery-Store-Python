__cnx = None
import mysql.connector

def get_sql_connection():

    global __cnx
    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='mysqlclarke@96',
                database='grocery_store'
            )
        except mysql.connector.Error as err:
            print(f"Database connection error: {err}")
            __cnx = None
    return __cnx
