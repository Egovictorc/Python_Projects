import mysql.connector as mysql

conn = mysql.connect(host="localhost",
                     user="root",
                     password="1234",
                     database="niit")
print(conn)
cursor = conn.cursor()
#insert_row = "insert into student (name, program) values('uche', 'python')"
#cursor.execute(insert_row)

delete_row = "delete from student where id = 4"
cursor.execute(delete_row)
conn.commit()

select_row = "select * from student"
cursor.execute(select_row)
for student in cursor:
    print(student)