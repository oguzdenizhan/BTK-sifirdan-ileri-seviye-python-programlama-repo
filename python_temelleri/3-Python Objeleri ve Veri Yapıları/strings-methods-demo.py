website= "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#1 " hello world " karakter dizisinin baştaki ve sondaki boşlukları silin 

hello = ' Hello World '

hello = hello.strip()
hello = hello.lstrip() #sadece sol
hello = hello.rstrip() #sadece sağ

#website= website.lstrip("/htp:")
print(website)
print(hello)

#2 www.sadikturan.com içindeki sadikturan bilgisi dışındaki her karakteri sil
length = website.find("sadikturan")
name= website[length:length+10]
print(name)

w='www.sadikturan.com'.strip("wmoc.")
print(w) 

#3 course değişkeni tüm karakterleri küçük harf yap
course = course.lower()
print(course)

#4 website değişkeni içindeki a sayısı

numberA= website.count("a")
print(numberA)
result= website.count("www")
print(result)
result= website.count("www",0,10)
print(result)

#5 web sitesi www ile başlayıp com ile biriyor mu

isFinish= website.startswith("www")
print(isFinish) 
isFinish= website.endswith("com")
print(isFinish) 

#6 web sitesi içinde .com ifadesi var mi

isHas = website.find(".com")
print(isHas)
isHas = website.find(".com",0,20)
print(isHas)

isHas = course.rfind("python")
print(isHas)

isHas = website.index(".com")
print(isHas)
isHas = website.rindex(".com")
print(isHas)
#isHas = website.rindex(".comm") #toksa find gibi -1 döndürmez hata verir
#print(isHas)
#7 course içindeki karakterlerin  hepsi alfabetik mi
isAlpha=course.isalpha()
print(isAlpha)
result='Hello'.isalpha()
print(result)
result='123'.isdigit()
print(result)

#8 'Contents' ifadesini satırda 50 karakter içine yerleştir ve sağ soluna * ekle
c= 'Contents'.center(50,"*")
print(c)
c= 'Contents'.ljust(50,"*")
print(c)
c= 'Contents'.rjust(50,"*")
print(c)
#9 course içindeki tüm boşluklar yerine - ile değiştir

# course= course.replace(" ","-")
# print(course)

# course= course.replace(" ","-",5)
# print(course)
# course= course.replace(" ","")
# print(course)

#10 Hello World karakter dizisindei World yerine There yaz
hello2= "Hello World"
lng= hello2.find("World")

hello2= hello2[:lng] + "There!"
print(hello2)

hello2= "Hello World"
hello2 = hello2.replace("World","There")
print(hello2)
#11 course karakter dizisini boşluk karakterlerinden ayırın

course= course.split(" ")

print(course)


