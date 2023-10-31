# 1- Girilen bir sayinin 0-100 arasinda olup olmadigina kontrol ediniz.
# sayi= int(input("Sayı: "))
# result = (sayi>0) and (sayi<=100)
# print(f"Sayi 0 ile 100 arasında {result}")


# 2- Girilen bir sayinin pozitif çift sayı olup olmadigina kontrol ediniz.
# sayi= int(input("Sayı: "))
# pozCift= (sayi>0)and (sayi % 2 == 0)
# print(f"{sayi} değeri pozitif çift mi {pozCift}")

# 3- Email ve parola bilgileri ile giris kontrolü yapiniz
# email="email@sadikturan.com"
# parola ="abc123"
# girParola = input("Parola gir: ")
# girEmail = input("Email gir: ")

# result=(email==girEmail.strip().lower()) and (parola==girParola.strip().lower())
# print(f"Giriş Başarılı mı : {result}")

# 4- Girilen 3 sayiyı büyüklük olarak karsalastiriniz.
# sayi1= int(input("Sayı 1: "))
# sayi2= int(input("Sayı 2: "))
# sayi3= int(input("Sayı 3: "))
# max=0
# if(sayi1>max):
#     max=sayi1
# if(sayi2>max):
#     max=sayi2
# if(sayi3>max):
#     max=sayi3
# print("max deger: {} ".format(max))

#5 - Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayin:
# v1 = float(input("1. Vize Sınavı: "))
# v2 = float(input("2. Vize Sınavı: "))
# final= float(input("Final Sınavı: "))
# vOrt= ((v1+v2))/2*0.6
# fOrt= final*0.4
# puan=vOrt+fOrt
#Eger ortalama 50 ve üstündeyse geçti degilse kaldı yazdirin.
# if(puan>=50):
#     print("Geçti")
# else:
#     print("Kaldı")
#a-) Ortamalama 50 olsa bile final not en az 50 olmalidir
# if(puan>=50 and final>=50):
#     print("Geçti")
# else:
#     print("Kaldı")
#b-) Finalden 70 alindiginda ortalamanin önemi olmasin.
# if((puan>=50 and final>=50) or final>=70):
#     print("Geçti")
# else:
#     print("Kaldı")

# 6- Kisinin ad, kilo ve boy bilgilerini alip kilo indekslerini hesaplayiniz.
#Formül: (Kilo / boy uzunlugunun karesi)
#Asagidaki tabloya göre kisi hangi gruba girmektedir
#0-18.4 => Zayif
#18.5-24.9 => Normal
#25.0-29.9 => Fazla Kilolu
#30.0-34.9 => Sisman (Obez)

ad = input("Ad: ")
kilo = float(input("Kilo: "))
boy = float(input("Boy: "))

bkIndex= kilo/(boy**2)
print(bkIndex)
if(bkIndex>0 and bkIndex<=18.4):
    print(f"{ad} isimli kişinin boy kilo indexi {bkIndex} : Zayıf")
if(bkIndex>=18.5 and bkIndex<=24.9):
    print(f"{ad} isimli kişinin boy kilo indexi {bkIndex} : Normal")
if(bkIndex>=25.0 and bkIndex<=29.9):
    print(f"{ad} isimli kişinin boy kilo indexi {bkIndex} : Fazla Kilolu")
if(bkIndex>=30.0 and bkIndex<=34.9):
    print(f"{ad} isimli kişinin boy kilo indexi {bkIndex} : Şişman Obez")


