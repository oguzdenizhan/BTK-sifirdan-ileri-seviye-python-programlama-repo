import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
    cursor=connection.cursor()

    # cursor.execute("SELECT * FROM products")
    cursor.execute("SELECT name,price FROM products")

    # result =cursor.fetchall()
    # for product in result:
    #     # print(f"name: {product[1]} price: {product[2]}")
    #     print(f"name: {product[0]} price: {product[1]}")

    result =cursor.fetchone()
    print(f"name: {result[0]} price: {result[1]}")


getProducts()

