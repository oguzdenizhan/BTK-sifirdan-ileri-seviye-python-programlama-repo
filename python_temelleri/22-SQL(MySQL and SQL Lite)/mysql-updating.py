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

def getProductByInfo():
        connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
        cursor=connection.cursor()

        # sql = "SELECT COUNT(*) FROM Products"  #COUNT(name) desek yine aynı sonuç olur
        # sql = "SELECT AVG(price) FROM Products"  
        # sql = "SELECT SUM(price) FROM Products" 
        # sql = "SELECT MIN(price) FROM Products"  
        # sql = "SELECT MAX(price) FROM Products"  
        sql = "SELECT name,price FROM Products where price =(SELECT MAX(price) FROM Products)"  




        cursor.execute(sql)

        result = cursor.fetchone()

        print(f"result: {result[0]} price {result[1]}")

def updateProduct(id,name,price):
        connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
        cursor=connection.cursor()

        sql = "UPDATE products SET name= %s, price =%s where id= %s"  
        values =(name,price,id)
        cursor.execute(sql,values)
        try:
            connection.commit()
            print(f"{cursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print("Hata: ",err)
        finally:
            connection.close()
            print("Database bağlantısı kapandı.")


        

 
updateProduct(1,"Iphone 8",6000)