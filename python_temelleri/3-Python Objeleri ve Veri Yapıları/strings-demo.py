website= "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# course kaç karakter
lengthC =len(course)
print(lengthC)
# website içinden www karakterlerini çek
print(website[7:10])
# website içinden com karakterlerini çek
lengthWeb =len(website)
print(website[lengthWeb-3:lengthWeb])
# course içinden ilk 15 ve son 15 karakteri alın
print(course[:15])
print(course[lengthC-15:lengthC])
print(course[-15:])
# course ifadesini tersten yazın
result=course[::-1] # [::1 ] soldan sağa birer birer al demekti -1 yapınca sağdan sola oldu
print(result)

#ek bilgi 

s="12345"*5
print(s)
print(s[::5])

name ,surname, age, job = "Bora", "Yılmaz",32, "Mühendis"

# Benim adım Bora Yılmaz Yaşım 32 ve mesleğim müdendis yaz
print(f"Benim adım {name} {surname}. Yaşım {age} ve Mesleğim {job}.")
# Hello world ifadesindeki w  harfini W ile değiştirin
hello= "Hello world"
hello = hello[0:6] +"W"+ hello[-4:]
print(hello)

# abc ifadesini yan yana 3 defa yazdır
str="abc"
print(str*3)



