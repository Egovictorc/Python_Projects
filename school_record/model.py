from tkinter import *
import mysql.connector as connector
from mysql.connector import Error

dbinfo = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "NIIT"
}

class Model():
    def __init__(self):
        self.conn = ""
        self.cursor = ""
        try:
            self.conn = connector.connect(**dbinfo)
            self.cursor = self.conn.cursor()
        except Error as e:
            print(e)

    def get_records(self):
        self.cursor.execute("SELECT * FROM students")
        result = self.cursor.fetchall()
        return result
        for res in result:
            print(res)

    def add_records(self, record):
        sql_ins = f"insert into students (email, password) VALUES(%s, %s)"
        values = (record["email"], record["password"])
        self.cursor.execute(sql_ins, values)
