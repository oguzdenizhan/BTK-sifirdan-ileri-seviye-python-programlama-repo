x,y,z=2,5,10

numbers= 1,5,7,10,6

# 1- Kullanicidan aldiginiz 2 sayinin çarpimu ile x,y,z toplaminin farki nedir
a= int(input("ilk sayı: "))
b= int(input("ikinci sayı: "))

# a*=b
# toplam= x+y+z
# fark= a-toplam
# print(fark)
result= (a*b)-(x+y+z)
print(result)

# 2- y' nin x' e kalansiz bölümünü hesaplayiniz.

kalansiz= y//x
print(kalansiz)
# 3 - (x,y,z) toplaminin mod 3' ü nedir ?
toplam= x+y+z
toplam %=3
print(toplam)
# 4- y' nin x. kuvvetini hesaplayiniz.
kuvvet =y**x
print(kuvvet)
# 5- x, *y, z = numbers islemine göre z' nin küpü kaçtir ?
x,*y,z= numbers
küp =z**3
print(küp)
# 6- x, *y, z = numbers islemine göre y nin degerleri toplami kaçtir ?
toplam = y[0]+y[1]+y[2]
print(toplam)