import mysql.connector as mysql

conn = mysql.connect(host="localhost",
                     user="root",
                     password="1234",
                     database="niit")
print(conn)
cursor = conn.cursor()

create_tb = "create table if not exists student(id int primary key auto_increment, name varchar(255), program varchar(255))"
cursor.execute(create_tb)

show_tb = "show tables"
cursor.execute(show_tb)

for table in cursor:
    print(table)

#drop_tb = "drop table if exists student"
#cursor.execute(drop_tb)

#create_db = "create database if not exists niit"
#cursor.execute(create_db)

#show_db = "show databases"
#cursor.execute(show_db)
#for db in cursor:
#    print(db)

# db_list = []
# for db in cursor:
#     db_list.append(db)
#     #print(db)
# print(db_list)