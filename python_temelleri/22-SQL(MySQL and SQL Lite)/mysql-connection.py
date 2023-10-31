import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost", #192.58.45.54 onlline server
    user = "root",
    password = "My.123456.o",
    database = "denemedb"
)
# print(mydb)

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE denemedb")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(255))")
