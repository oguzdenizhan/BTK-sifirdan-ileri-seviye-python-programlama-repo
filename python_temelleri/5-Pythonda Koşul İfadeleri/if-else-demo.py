#1 - Kullanicidan isim, yaş ve egitim bilgilerini isteyip ehliyet alabilme
#durumunu kontrol ediniz. Ehliyet alma kosulu en az 18 ve egitim durumu
#lise ya da universite olmalidir.
# ad= input("Ad: ")
# yas= int(input("Yaş: "))
# egitim= input("Eğitim durumu: ")

# if(yas>=18):
#     if(egitim=="üniversite" or egitim=="lise"):
#         print("Ehliyet alabilir")
#     else:
#         print(f"{ad} Ehliyet alamazsınız eğitim seviyeniz tutmuyor")
# else:
#     print(f"{ad} Ehiyet alamazsiniz yaş tutmuyor")



#2 - Bir ögrencinin 2 yazilı bir sözlü notunu alip hesaplanan ortalamaya göre
#n ot araligina karsılik gelen not bilgisini yazdiriniz.
# 0- 24 => 0
# 25-44 =›  1
# 45-54 =›  2
# 55-69 =›  3
# 70-84 =>  4
# 85-100 => 5

# yazili1 = int(input("1. Yazılı: "))
# yazili2 = int(input("2. Yazılı: "))
# sozlu = int(input("Sözlü: "))

# ortalama =(yazili1+yazili2+sozlu)/3

# if(ortalama>=0 and ortalama<=24):
#     print("0")
# elif(ortalama>=25 and ortalama<=44):
#     print("1")    
# elif(ortalama>=45 and ortalama<=54):
#     print("2")   
# elif(ortalama>=55 and ortalama<=69):
#     print("3")   
# elif(ortalama>=70 and ortalama<=84):
#     print("4") 
# elif(ortalama>=85 and ortalama<=100):
#     print("5") 
# else:
#     print("Yanlis işlem") 
  
# 3- Trafige cakis tarihi alinan bir aracin servis zamanin asagidaki bilgilere
# göre hesaplayiniz.
# 1. Bakim => 1. yı1
# 2. Bakim => 2. yıl
#  3. Bakim => 3. yıl
# ** Süre hesabini alinan gün, ay, yil bilgisine göre gün bazli hesaplayin
# *** datetime modülünü kullanmaniz gerekiyor.

#çözüm ben
# import datetime
# year =int(input("Yıl:"))
# month =int(input("Ay:"))
# day =int(input("Gün:"))

# x = datetime.datetime(year, month, day)
# y= datetime.datetime.now()
# z= y-x
# # print(x)
# # print(y)
# # print(z)

# bakim= z/365
# print(f"{bakim.days}. yıl")

#çözüm hoca

import datetime

tarih= input("aracınız hangi tarihte trafiğe çıktı (2019/8/9): ")
tarih = tarih.split("/")
trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi= datetime.datetime.now()
fark= simdi-trafigeCikis
days=fark.days

if days<=365:
    print('1. Servis aralığı')
elif days >365 and days<=365*2:
    print('2. Servis aralığı')
elif days >365*2 and days<=365*3:
    print('3. Servis aralığı')
else:
    print("hatalı tarih")
