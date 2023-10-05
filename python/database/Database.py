import mysql.connector
from mysql.connector import Error
class Database(object):
            
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
            print("Creating Database instance")
        return cls._instance

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",
                database = "bd_design",
                user = "root",
                password = ""
            )

        except Error as e:
            print("Error" + e)

    def insert(self, itens, table):
        pass

    def select(self, table):
        pass

    def update(self, itens, table):
        pass

    def delete(self, itens, table):
        pass