from mysql.connector import connect
from contextlib import contextmanager

config_db = dict(host="localhost", port="6006", user="root", database="music")


@contextmanager
def db_connect():
    connection = connect(**config_db)
    try:
        yield connection
    finally:
        if connection and connection.is_connected():
            connection.close()
