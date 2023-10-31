import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
    cursor=connection.cursor()

    # cursor.execute("SELECT * FROM products Order By name")
    # cursor.execute("SELECT * FROM products Order By price")
    # cursor.execute("SELECT * FROM products Order By id DESC") #DESC AZALAN ASC  ARTAN 
    cursor.execute("SELECT * FROM products Order By name,price")

    try:
        result =cursor.fetchall()
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")
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


# getProductByid(1)

getProducts()