import numpy as np
# 1- (10, 15, 30,45,60) degerlerine sahip numpy dizisi olusturunuz.
result = np.array([10,15,30,45,60])

# 2- (5-15) arasindaki sayilarla numpy dizisi olusturunuz.
result= np.arange(5,15)
# 3- (50-100) arasinda 5'er 5'er artarak numpy dizisi olusturunuz.
result= np.arange(50,100,5)

# 4- 10 elemanli sifirlardan olusan bir dizi olusturunuz.
result= np.zeros(10)
# 5- 10 elemanla birlerden olusan bir dizi olusturunuz.
result= np.ones(10)

# 6- (0-100) arasinda sit aralikla 5 say üretin.
result= np.linspace(0,100,5)

# 7 - (10-30) arasinda rastgele 5 tane tamsayi üretin.
result = np.random.randint(10,30,5)

# 8- [-1 ile 1] arasinda 10 adet sayi üretin.
result = np.random.randn(10)

# 9- (3x5) boyutlarinda (10-50) arasinda rastgele bir matris olusturunuz.
matris = np.random.randint(10,50,15).reshape(3,5)

# print(matris)

# 10- Üretilen matrisin satir ve sütun sayilara toplamlarina hesaplayiniz?
# print(f"Matris: {matris}")
# satir = matris.sum(axis=1)
# print(f"satır toplamı: {satir}")
# sutun = matris.sum(axis=0)
# print(f"sütun toplamı: {sutun}")
# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?
max = matris.max()
min = matris.min()
mean= matris.mean()
# print(f"max {max} min {min} mean {mean}")

# 12- Üretilen matrisin en büyük degerinin indeksi kaçtir?
result = matris.argmax()

# 13- (10-20) arasindaki sayilar içeren dizinin ilk 3 elemanina seçiniz.
arr = np.arange(10,20)
# print(arr)
# print(arr[:3])

# 14- Üretilen dizinin elemanlarina tersten yazdirin.
# print(arr[::-1])

# 15- Üretilen matrisin ilk satirina seçiniz.
# print(matris)
# print(matris[0])

# 16- Üretilen matrisin 2.satir 3.sütundaki eleman hangisidir ?
# print(matris[1][2])
# print(matris[1,2])


# 17 - Üretilen matrisin tüm satirlardaki ilk elemani seçiniz.
result=matris[:,0]
# 18- Üretilen matrisin her bir elemaninin karesini aliniz.
result = matris**2
# 19- Üretilen matris elemanlarinin hangisi pozitif çift sayidir ?
#Aralig1 (-50, +50) arasinda yapin1z.
matris = np.random.randint(-50,50,15).reshape(3,5)
print(matris)

ciftler= matris[matris %2 ==0]
result = ciftler[ciftler>0]

print(result)