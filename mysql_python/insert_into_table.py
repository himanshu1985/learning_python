import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Cheetah@123",
    database="my_database",
)
my_cursor = mydb.cursor()
sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
val = [
    ("Himanshu", "A 102 PKT 3"),
    ("Prabhanshu", "Kailash kunj bareilly"),
    ("Shashi", "3 rd lane Bareilly"),
    ("Nidhi", "near school Budaun")
    ]
my_cursor.executemany(sql, val)

mydb.commit()
print(my_cursor.rowcount, "row inserted")
print("1 record inserted, ID: ", my_cursor.lastrowid)

