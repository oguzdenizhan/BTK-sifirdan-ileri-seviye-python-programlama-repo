# 1- Girilen 2 sayidan hangisi büyüktür ?
# sayi1 = int(input("Sayı 1: "))
# sayi2 = int(input("Sayı 2: "))
# if(sayi1>sayi2):
#     print("{} büyüktür".format(sayi1))
# elif(sayi2>sayi1):
#     print("{} büyüktür".format(sayi2))

# else:
#     print("Eşitler")

# 1- Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayin1z
# v1 = float(input("1. Vize Sınavı: "))
# v2 = float(input("2. Vize Sınavı: "))
# final= float(input("Final Sınavı: "))
# vOrt= ((v1+v2))/2*0.6
# fOrt= final*0.4
# puan=vOrt+fOrt
# Eger ortalama 50 ve üstündeyse geçti degilse kaldı yazdirin.
# if(puan>=50):
#     print("{} Puan ile Geçti".format(puan))

# else:
#     print("{} Puan ile Kaldı".format(puan))

# 3- Girilen bir sayinin tek mi çift mi oldugunu yazdirin.
# sayi = int(input("Sayı gir: "))
# if(sayi % 2 == 0):
#     print("Sayı Çift")
# else:
#     print("Sayı Tek")

# 4- Girilen bir sayinin negatif pozitif durumunu yazdirin.
# sayi = int(input("Sayı gir: "))
# if(sayi < 0):
#     print("Sayı Negatif")
# elif(sayi>0):
#     print("Sayı Pozitif")
# else:
#     print("Sayı Nötr (0)")

#5- Parola ve email bilgisini isteyip dogrulugunu kontrol ediniz.
parola = input("Parola gir: ")
email = input("Email gir: ")
if("email@sadikturan.com"==email.strip() and "abc123"==parola.strip() ):
    print("Doğru")
else:
    print("Yanlış")
#(email: email@sadikturan.com parola: abc123)