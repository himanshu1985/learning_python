import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Cheetah@123",
    database="my_database",
)
my_cursor = mydb.cursor()

my_cursor.execute("SELECT name, address FROM customers")
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)
#  sql = 'SELECT * FROM customers WHERE address =  "Kailash kunj bareilly"'
#  sql = 'SELECT * FROM customers WHERE address LIKE "%Kailash%"'
#  my_cursor.execute(sql)
#  my_result = my_cursor.fetchall()
#  for x in my_result:
#     print(x)
#  my_cursor.execute("SELECT * FROM customers")
#  my_result = my_cursor.fetchone()
#  print((my_result)

