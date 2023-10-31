# x = input("1. Sayı: ")
# y = input("2. Sayı: ")

# print(type(x))
# print(type(y))
# toplam =int(x) +int(y)
# print(toplam)


pi = 3.14
r= input("Yarıçap Girin: ")
r= float(r) 

DaireAlan = pi*(r**2)
DaireCevre = 2*pi*r

print("Daire Alan: ",DaireAlan)
print("Daire Çevre: ",DaireCevre)

print("Daire Alan: "+ str(DaireAlan) +" "+ "Daire Çevre: " + str(DaireCevre))