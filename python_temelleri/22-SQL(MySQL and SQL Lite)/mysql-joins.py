import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
    cursor=connection.cursor()
    # sql= "SELECT * FROM products"
    # sql= "SELECT * FROM categories"
    # sql= "SELECT * FROM products inner join categories on categories.id=products.categoryId"
    # sql = "SELECT products.name,products.price,categories.name FROM products inner join categories on categories.id=products.categoryId"
    # sql = "SELECT products.name,products.price,categories.name FROM products inner join categories on categories.id=products.categoryId where categories.name='Telefon'"
    sql = "SELECT p.name,p.price,c.name FROM products as p inner join categories as c on c.id=p.categoryId where p.name='samsung S5'"
    

    cursor.execute(sql)

    try:
        result =cursor.fetchall()
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")
    for product in result:
        print(product)
def getProductByid(id):
        connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
        cursor=connection.cursor()

        sql = "SELECT * FROM Products where id =%s"  
        params=(id,)

        cursor.execute(sql,params)

        result = cursor.fetchone()

        print(f"id: {result[0]} name: {result[1]} price: {result[2]}")



getProducts()