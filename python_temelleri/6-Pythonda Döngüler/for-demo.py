sayilar = [1,3,5, 7,9, 12, 19, 21]
# 1- Sayilar listesindeki hangi sayilar 3'ün katidir ?

# #1
# for i in sayilar:
#     if(i%3==0):
#         print(i)
# #2
# liste =[]
# for i in sayilar:
#     if(i%3==0):
#         liste.append(i)
# print(f"3'ün katları {liste}")
# 2- Sayilar listesinde sayilarin toplamı kactir ?
# toplam=0
# for i in sayilar:
#     toplam+=i
# print(toplam)
# 3- Sayilar listesindeki tek sayilarin karesini alınız.
# kare=0
# for i in sayilar:
#     if(i%2==1):
#         kare=i**2
#         print(kare)

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir','rize']
# 4- Sehirlerden hangileri en fazla 5 karakterlidir ?
# for sehir in sehirler:
#     if(len(sehir)<=5):
#         print(sehir)

urunler = [
{'name': 'samsung $6', "price": "3000"},
{'name': 'samsung S7', 'price': '4000' },
{'name': 'samsung S8', 'price': '5000' },
{'name': 'samsung S9', 'price': '6000' },
{'name': 'samsung s10', 'price': '7000' }
]

#5 ürünlerin fiyatlarının toplamı nedir
toplam=0
for urun in urunler:
    fiyat= int(urun["price"])
    toplam+= fiyat
print(toplam)

#6 ürünlerin fiyatı  en fazla 5000  olanları göster
for urun in urunler:
    fiyat= int(urun["price"])
    if(fiyat<=5000):
        print(urun["name"])

