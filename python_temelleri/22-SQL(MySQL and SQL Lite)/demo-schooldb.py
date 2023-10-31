# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)
import mysql.connector
from datetime import datetime
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "My.123456.o",
    database = "schooldb"
)

mycursor = connection.cursor()

# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.
# ("101","Ahmet","Yılmaz",datetime.datetime(2005,5,17),"E")
# ("102","Ali","Can",datetime.datetime(2005,6,17),"E")
# ("103","Canan","Tan",datetime.datetime(2005,7,17),"K")
# ("104","Ayşe","Taner",datetime.datetime(2005,9,23),"K")
# ("105","Bahadır","Toksöz",datetime.datetime(2004,7,27),"E")
# ("106","Ali","Cenk",datetime.datetime(2003,8,25),"E")

sql = "INSERT INTO student(studentNumber,name,surname,birthdate,gender) VALUES (%s,%s,%s,%s,%s)"

ogrenciler =[

    ("101","Ahmet","Yılmaz",datetime(2005,5,17),"E"),
    ("102","Ali","Can",datetime(2005,6,17),"E"),
    ("103","Canan","Tan",datetime(2005,7,17),"K"),
    ("104","Ayşe","Taner",datetime(2005,9,23),"K"),
    ("105","Bahadır","Toksöz",datetime(2004,7,27),"E"),
    ("106","Ali","Cenk",datetime(2003,8,25),"E")

]

mycursor.executemany(sql, ogrenciler)

try:
    connection.commit()
    print(f"{mycursor.rowcount} tane kayıt eklendi ")
except mysql.connector.Error as err:
    print("hata ",err)
finally:
    connection.close()
