names = ['Ali', 'Yagmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]
# 1-"'Cenk"' ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)
# 2-"Sena"' degerini listenin basina ekleyiniz.
names.insert(0,"Sena")
#en sona eklemek için ayrıca
names.insert(len(names),"Mehmet")
#names.insert(0,"Sena")
print(names)
# 3-"Deniz" ismini listeden siliniz.
#names.pop(-2)
#names.remove("Deniz")
# index = names.index("Deniz")
# names.pop(index)
# print(names)
# 4-"Deniz" isminin indeksi nedir ?
index = names.index("Deniz")
print("index",index)
# 5-"Ali" listenin bir elemani midir?
result = "Ali" in names
print(result)
index = names.index("Ali")
print(index)
# 6-Liste elemanlarini ters çevirin.
names.reverse()
print(names)
# 7-Liste elemanlarini alfabetik olarak siralayin1z.
names.sort()
print(names)
# 8-years listesini rakamsal büyüklüge göre siralayiniz.
years.sort()
print(years)
# 9-str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet, Dacia"
str=str.split(",")
print(str)
#10- years dizisinin en büyük ve en küçük elemani nedir?
max=max(years)
min=min(years)
print(f"Max {max} and Min {min}")
# 11- years dizisinde kaç tane 1998 degeri vardir ?
howMany = years.count(1998)
print(howMany)
# 12- years dizisinin tüm elemanlarin siliniz.
#years.clear()
print(years)
# 13 - Kullanicidan alacaginiz 3 tane marka bilgisini bir listede saklayiniz.
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
print(markalar)
