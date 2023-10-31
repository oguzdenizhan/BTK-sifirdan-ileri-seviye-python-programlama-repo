"""
1-100 araslnda rastgele üretilecek bir sayıyı asagı yukarı ifadeleri ile
buldurmaya calışın. (hak = 5)
**"random modülü" icin "python random" seklinde arama yap.
**100 üzerinden puanlama yapın. Her soru 20 puan.
**Hak bilgisini kullanıcıdan alin ve her soru belirtilen can sayısı üzerinden hesaplansln.
"""

# import random

# rastgele = random.randint(1,100)

# hak =5
# totalPuan=100
# puan =totalPuan/hak
# while(hak>0):
#     tahmin=int(input("Tahminizi giriniz: "))
#     if(rastgele>tahmin):
#         print("Yukarı")
#         totalPuan-=puan
#     elif(rastgele<tahmin):
#         print("Aşağı")
#         totalPuan-=puan
#     else:
#         print("Tebrikler bildiniz..")
#         hak=0
#     hak -=1
# print(f"Toplam Puannınız {totalPuan}")


import random

rastgele = random.randint(1,10)

hak = int(input("Hak sayısı giriniz: "))
totalPuan=100
puan =totalPuan/hak
sayac =0
while(hak>0):
    hak -=1
    sayac+=1
    tahmin=int(input("Tahminizi giriniz: "))
    if(rastgele>tahmin):
        print("Yukarı")
        totalPuan-=puan
    elif(rastgele<tahmin):
        print("Aşağı")
        totalPuan-=puan
    else:
        print(f"Tebrikler {sayac}. defada bildiniz..")
        break
    if hak==0:
        print(f"Hakkınız biti tutulan sayı: {rastgele}")
print(f"Toplam Puannınız {totalPuan}")   
