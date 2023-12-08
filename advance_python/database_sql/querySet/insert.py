import dbconnection

dbconnection.mycursor.execute('insert into users (first_name, last_name, email, mobile, age) values ("brijesh", "gondaliya", "brijesh@gmail.com", "7676767676", 27);')
dbconnection.db.commit()