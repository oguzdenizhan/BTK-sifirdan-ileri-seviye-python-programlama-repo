
import mysql.connector
from datetime import datetime
from connection import connection



class Student:
    connection = connection
    mycursor = connection.cursor()
    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthday = birthdate
        self.gender = gender
    def saveStudent(self):
        sql = "INSERT INTO student(studentNumber,name,surname,birthdate,gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthday,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi ")
        except mysql.connector.Error as err:
            print("hata ",err)
        finally:
            Student.connection.close()
    @staticmethod       
    def saveStudents(students):
        sql = "INSERT INTO student(studentNumber,name,surname,birthdate,gender) VALUES (%s,%s,%s,%s,%s)"
        value = students
        Student.mycursor.executemany(sql,value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi ")
        except mysql.connector.Error as err:
            print("hata ",err)
        finally:
            Student.connection.close()
    @staticmethod
    def StudentInfo():
        # 4- Aşağıdaki sorguları yazınız.
        #   a- Tüm öğrenci kayıtlarını alınız.
        sql="SELECT * FROM student"
        sql="SELECT * FROM student LIMIT 5"

        #   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
        sql="SELECT studentNumber,name,surname FROM student"

        #   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
        sql="SELECT name,surname FROM student where gender ='K'"

        #   d- 2003 doğumlu öğrenci bilgilerini alınız. 
        sql="SELECT * FROM student WHERE YEAR(birthdate) = 2003"

        #   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
        sql="SELECT * FROM student WHERE name ='Ali' AND YEAR(birthdate) = 2005"

        #   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
        sql="SELECT * FROM student WHERE name LIKE '%an%'  OR surname LIKE'%an%'"

        #   g- Kaç erkek öğrenci vardır ?
        sql = "SELECT COUNT(*) FROM student where gender ='E'"
        #   h- Kız öğrencileri harf sırasına göre getiriniz.
        sql="SELECT * FROM student where gender ='K' ORDER BY name,surname"


        Student.mycursor.execute(sql)
        try:
            result = Student.mycursor.fetchall()
            for student in result:
                print(student)
        except mysql.connector.Error as err:
            print("hata ",err)
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentById(id):
        sql = "Select * FROM student where id =%s"
        value=(id,)

        Student.mycursor.execute(sql,value)
        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print("hata",err)
    @staticmethod
    def getStudentByGender(gender):
        sql = "Select * FROM student where gender =%s"
        value=(gender,)

        Student.mycursor.execute(sql,value)
        try:
            return Student.mycursor.fetchall()
            
        except mysql.connector.Error as err:
            print("hata",err)

    def updateStudent(self):

        sql="update student set studentNumber=%s, name=%s,surname=%s,birthdate=%s,gender=%s where id = %s"
        values=(self.studentNumber,self.name,self.surname,self.birthday,self.gender,self.id)

        Student.mycursor.execute(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellenmiştir.")
        except mysql.connector.Error as err:
            print("hata: ",err)

    @staticmethod
    def updateStudents(liste):

        sql="update student set studentNumber=%s, name=%s,surname=%s,birthdate=%s,gender=%s where id = %s"
        values= []
        order= [1,2,3,4,5,0]
        for item in liste:
            item= [item[i] for i in order]
            values.append(item)
        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellenmiştir.")
        except mysql.connector.Error as err:
            print("hata: ",err)


# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
# student= Student.getStudentById(7)

# student.name="Çınar"
# student.surname= "Yılmazer"

# student.updateStudent()

#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

students= Student.getStudentByGender("E")

liste = []
for std in students:
    std = list(std)
    std[2]= "Mr. "+std[2]
    liste.append(std)

Student.updateStudents(liste)