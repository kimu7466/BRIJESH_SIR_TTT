import dbconnection

def create_table():
    table_name = input('Enter a table name: ')
    fields_configuration = ''

    flag = True
    while flag:
        yn = input("y/n: ")
        if yn.lower() == 'y':
            addField = input("Enter a field config : ")
            fields_configuration+=addField + ','
        else:
            flag = False
            
    sql = f'create table {table_name} ({fields_configuration});'
    modified_sql = sql[-4::-1][::-1] + sql[-2:]
    return modified_sql

dbconnection.mycursor.execute(create_table())