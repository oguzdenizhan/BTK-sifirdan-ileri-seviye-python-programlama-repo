#1 list oluştur
cars=["Bmw","Mercedes","Opel","Mazda"]
print(cars)
#2 eleman sayısı
print(len(cars))
#3 ilk ve son eleman
print(f"ilk eleman {cars[0]}, son eleman {cars[-1]}")
#4 mazda ile toyota yer değiştir
cars[3]="Toyota"
print(cars)
#5 mercedes listenin  bir elemanı mı
isElement ="Mercedes" in cars
print(isElement)
#6 listenin -2 indeksindeki değer
print(cars[-2])
#7 listenin ilk 3 elemanını al
print(cars[:3])
#8listenin son 2 elemanı yerine toyota ve renault değerleri ekle
cars[-2:]="Toyota","Renault"
print(cars)
#9listenin üzerine Audi ve nissan değerlerini ekle
ekle =cars + ["Audi","Nissan"]
print(ekle)
#10listenin son elemanını sil
del cars[-1]
print(cars)

#11listenin  elemanlarını tersten yazdırdın
tersten= cars[::-1]
print(tersten)
#12 aşağıdaki  veriler liste içinde sakla
studentA=["Yiğit","Bilgi", 2010,[70,60,70]]
studentB=["Sena", "Turan", 1999,[80,80,70]]
studentC=["Ahmet", "Turan", 1998,[80,70,70]]

students= [studentA,studentB,studentC]
#13 Liste elemanlarını ekrana yaz
print(students)
print(students[0])
print(students[1])
print(students[2])
print(studentC[3][1])
# yiğit bilgi 13 yaşında ne not ortalaması 66
age=2023-studentA[2]
average= ((studentA[3][0]+studentA[3][1]+studentA[3][2])/3)
averageR=average_rounded = round(average, 2)
print(average)

print("the average is {a:.4}".format(a=average))
print(f"{studentA[0]} {studentA[1]} {2023-studentA[2]} yaşında ve not ortalaması {averageR}")

