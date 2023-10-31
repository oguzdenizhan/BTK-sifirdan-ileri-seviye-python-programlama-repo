# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazin.

#1
# def tekrarYaz(kelime,adet):
#     for i in range(adet):
#         print(kelime)
# x=input("kelime gir: ")
# y= int(input("kaç defa: "))

# tekrarYaz(x,y)

#2
# def yazdir(kelime,adet):
#     print(kelime*adet)

# yazdir("Merhaba\n",5)

# 2- Kendine gönderilen sinirsiz sayidaki parametreyi bir listeye çeviren fonks


# def listeyeCevir(*params):
#     liste= []
#     for param in params:
#         liste.append(param)

#     return liste

# result=listeyeCevir("ali",23,45,"İstanbul")
# print(result)
# 3- Gönderilen 2 say arasindaki tüm asal sayilar bulun.



# def asalBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if( sayi%i==0):
#                     break
#             else:
#                 print(sayi)
    

# sayi1= int(input("sayı 1: "))
# sayi2= int(input("sayı 2: "))
# asalBul(sayi1,sayi2)

# 4- Kendisine gönderilen bir sayinin tam bölenlerini bir liste seklinde döndür

def tamBolen(sayi):
    tam=[]
    for i in range(2,sayi):
        if(sayi%i==0):
            tam.append(i)
    return tam
        
print(tamBolen(20))