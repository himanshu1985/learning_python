import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Cheetah@123",
    database="my_database",
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE customers(id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR (255), address VARCHAR(255))")

#  my_cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#  Create primary key on an existing table