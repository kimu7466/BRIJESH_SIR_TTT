import mysql.connector

db = mysql.connector.connect(user='root', password='root',
                              host='localhost', database='assignment_mod_5')
mycursor = db.cursor()