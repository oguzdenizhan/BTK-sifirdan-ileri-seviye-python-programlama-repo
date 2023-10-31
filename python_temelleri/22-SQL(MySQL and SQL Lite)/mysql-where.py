import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
    cursor=connection.cursor()

    # cursor.execute("SELECT * FROM products WHERE id=1")
    # cursor.execute("SELECT * FROM products WHERE name='Samsung S5' and price>='1000'")
    # cursor.execute("SELECT * FROM products WHERE name='Samsung S5' or price='3000'")
    # cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung%'")
    # cursor.execute("SELECT * FROM products WHERE name LIKE 'Samsung%'")
    # cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung'")
    cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung%' and price =3000")






    result =cursor.fetchall()
    print(result)
    for product in result:
        print(f"id: {product[0]} name: {product[1]} price: {product[2]}")
def getProductByid(id):
        connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
        cursor=connection.cursor()

        sql = "SELECT * FROM Products where id =%s"  
        params=(id,)

        cursor.execute(sql,params)

        result = cursor.fetchone()

        print(f"id: {result[0]} name: {result[1]} price: {result[2]}")


# getProducts()

# getProductByid(1)