import mysql.connector

def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
    cursor=connection.cursor()

    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Eklenen son kaydın idsi : {cursor.lastrowid}")

    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

def insertProducts(list):
    connection = mysql.connector.connect(host = "localhost",user="root", password = "My.123456.o", database = "node-app")
    cursor=connection.cursor()

    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (list)

    cursor.executemany(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Eklenen son kaydın idsi : {cursor.lastrowid}")

    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

list =[]
while True:
    name = input("urün adı: ")
    price = float(input("urün fiyatı: "))
    imageUrl = input("urün resim adı: ")
    description = input("urün açıklaması: ")
    list.append((name,price,imageUrl,description))

    result = input("Devam etmek istiyor musunuz (e/h)")
    if result=="h":
        print("Kayıtlarınız aktarılıyor")
        print(list)
        insertProducts(list)
        break


# insertProduct(name,price,imageUrl,description)

