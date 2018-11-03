import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Cheetah@123",
    database="my_database",
)
my_cursor = mydb.cursor()

#  sql = 'SELECT * FROM customers ORDER BY name'
sql = 'SELECT * FROM customers ORDER BY name DESC'
my_cursor.execute(sql)
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)