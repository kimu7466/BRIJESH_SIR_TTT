import mysql.connector

db = mysql.connector.connect(user='root', password='root',
                              host='localhost', database='register')
mycursor = db.cursor()