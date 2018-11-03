import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Cheetah@123",
    database="my_database",
)
my_cursor = mydb.cursor()

sql = 'DROP TABLE ramesh'
#  sql = "DROP TABLE IF EXISTS customers"
my_cursor.execute(sql)
