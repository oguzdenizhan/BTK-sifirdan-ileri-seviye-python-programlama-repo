sayilar = [1, 3,5,7,9, 12, 19, 21]
# 1: sayilar listesini while ile ekrana yazdirin.
# x=0
# while(x<len(sayilar)):
#     print(sayilar[x])
#     x+=1

# 2: Baslangiç ve bitis degerlerini kullanicidan alip aradaki tüm
#tek sayilari ekrana yazdirin.

# baslangic= int(input("Başlangıç değeri gir: "))
# bitis= int(input("Bitiş değeri gir: "))
# while(baslangic<=bitis):
#     if(baslangic%2==1):
#         print(baslangic)
#     baslangic+=1


# 3: 1-100 arasindaki sayilar azalan sekilde yazdirin.
# x=1
# while(x<=100):
#     print(x)
#     x=x+1

 #4: Kullanicidan alacaganiz 5 sayıyı ekranda sirala bir sekilde yazdirin.
# liste1=[]
# x=0
# while(x<5):
#     sayi=int(input("Sayı girin:"))
#     liste1.append(sayi)
#     x+=1

# liste1.sort()
# print(liste1)



# 5: Kullanicidan alacaginiz sinirsiz ürün bilgisini urunler listesi içinde sak
#* ürün sayisinı kullaniclya sorun.
#** dictionary listesi yapis1 (name, price) seklinde olsun.
#*** ürün ekleme islemi bittiginde ürünleri ekranda while ile listeleyin.

urunler= []
adet= int(input("Kaç adet ürün eklemek istiyorsunuz: "))
x=0
while(x<adet):
    name= input("ürün ismi: ")
    fiyat= int(input("fiyat: "))
    urunler.append({
        "name":name,
        "price":fiyat
    })
    x+=1

for urun in urunler:
    print(f"Ürün adı: {urun['name']} Urün fiyatı: {urun['price']}")
