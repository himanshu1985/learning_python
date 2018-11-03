import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Cheetah@123",
    database="my_database",
)
my_cursor = mydb.cursor()
#  my_cursor.execute('SELECT * FROM customers LIMIT 1')
my_cursor.execute('SELECT * FROM customers LIMIT 2 OFFSET 1')
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)