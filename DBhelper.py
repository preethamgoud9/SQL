import sys

import mysql.connector
import sys
class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hit-demo"
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database successfully")  # Moved this inside try
        except:
            print("some error has occurred")
            sys.exit(0)
        else:
            print("connected to database")

    def register(self,name,email,password):
        try:
            self.cursor.execute(
            "INSERT INTO `hit-demo` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');"
            .format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
