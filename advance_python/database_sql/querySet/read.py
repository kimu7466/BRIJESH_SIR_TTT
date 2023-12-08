import dbconnection

dbconnection.mycursor.execute('select * from users')

for user in dbconnection.mycursor.fetchall():
    print(list(user))