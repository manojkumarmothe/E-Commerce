from tkinter import *
from tkinter import messagebox
import pymysql


def login_call():
    root = Tk()
    ob = Login(root)
    root.mainloop()


def database():
    global mydb, mycursor
    mydb = pymysql.connect(host='localhost', user='root', password='root')
    mycursor = mydb.cursor()
    mycursor.execute('create database if not exists e_commerce1')

    mycursor.execute('use e_commerce1')
    mycursor.execute("create table if not exists Registration_copy (FirstName varchar(50), LastName varchar(50),"
                     " Password varchar(20), Email varchar(50), Mobile bigint(20))")
    mycursor.execute('create table if not exists data(id INT,name VARCHAR(100),phone FLOAT(9,2),descr VARCHAR(100))')
    mycursor.execute("create table if not exists cart (Email varchar(30), pid int(5),"
                           "pname varchar(100),pprise float(10,2))")
    sql = "insert into registration_copy values (%s,%s,%s,%s,%s)"
    value = ("admin", "admin", "admin123", "admin@gmail.com", "9999999999")
    mycursor.execute(sql, value)
    mydb.commit()


if __name__ == '__main__':
    database()
    login_call()
