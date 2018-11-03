import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Cheetah@123",
    database="my_database",
)
my_cursor = mydb.cursor()
sql = 'UPDATE customers SET address = "nekpur budaun" WHERE address = "near school budaun"'

my_cursor.execute(sql)
mydb.commit()
print(my_cursor.rowcount, "records affected")
