import mysql.connector
from mysql.connector import Error
class Db(object):
            
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Db, cls).__new__(cls, *args, **kwargs)
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

    def select(self, table, where=None, order=None, limit=None, fields=None):
        try:
            cursor = self.conn.cursor()
            
            sql = "SELECT "
                
            if fields == None:
                sql += "* "
            else:
                sql += fields + " "
            
            sql += "FROM " + table + " "

            if where != None:
                sql += "WHERE " + where + " "
            
            if order != None:
                sql += "ORDER BY " + order + " "
            
            if limit != None:
                sql += "LIMIT " + limit + " "
            
            cursor.execute(sql)

            return cursor.fetchall()
        
        except Error as e:
            print("Error")


if __name__ == '__main__':
    Database = Db()
    result = Database.select("cliente", None, "cpf", "0,3")
    for x in result:
        print(x)