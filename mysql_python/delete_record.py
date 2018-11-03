import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Cheetah@123",
    database="my_database",
)
my_cursor = mydb.cursor()
#  sql = "DELETE FROM customers WHERE id = 8"
sql = "DELETE FROM customers WHERE address = 'Kailash kunj bareilly'"
my_cursor.execute(sql)
mydb.commit()
print(my_cursor.rowcount, "records deleted")