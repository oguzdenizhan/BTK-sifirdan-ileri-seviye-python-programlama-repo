liste = ["1", "2", "5a","10b" , "abc","10","50"]
# 1: Liste elemanlar içindeki sayisal degerleri bulunuz.

#Ben
# import re
# for value in liste:

#     if re.search("[a-z]",value):
#         continue
#     elif re.search("[A-Z]",value):
#         continue
#     else:
#         print(value)
#Hoca
# for x in liste:
#     try:
#         result =int(x)
#         print(result)
#     except ValueError:
#         continue

# 2: Kullanic1 'q' degerini girmedikçe aldiğınız her inputun sayı
# oldugundan emin olunuz aksi halde hata mesaja yazin.

# while True:
#     sayi = input("Sayı giriniz: ")
#     if sayi=="q":
#         break
#     try:
#         result= float(sayi)
#         print("Girdiğiniz sayı",result)
#     except ValueError:
#         print("Sadece sayı değeri giriniz")
#         continue


# 3: Girilen parola içinde türkçe karakter hatası veriniz.

# ben
# import re
# def checkTurkishCharacter(psw):
#     if re.search("[ğĞüÜşŞİıçÇöÖ]",psw):
#         raise Exception("parola Türkçe karakter  içermemelidir")



# password = "Oguzhan"
# try:
#     checkTurkishCharacter(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola else")

#hoca
# def CheckPassword(parola):
#     turkce_karakterler = 'şçğüöİı'

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError('Parola türkçe karakter içeremez. ')
#         else:
#             pass
#     print('geçerli parola')


# parola = input ('parola: ')
# try:
#     CheckPassword(parola)
# except TypeError as err:
#     print(err)

# 4: Faktöriyel fonksiyonu olusturup fonksiyona gelen deger için
# hata mesajlara verin.


# import re
# def Factorial(x):
#         faktoriyel=1
#         while x>0:
#             faktoriyel *= x
#             x-=1
#         print(f"Faktöriyel = {faktoriyel}")

# try:
#     input = input("Sayı girin: ")
#     if re.search("[a-z]",input):
#         raise Exception("Sadece sayı değeri giriniz.")
#     elif re.search("[A-Z]",input):
#         raise Exception("Sadece sayı değeri giriniz.")
#     elif  re.search("[_@$]",input):
#         raise Exception("Girdiğiniz değer alpha numeric değer içermemelidir")
#     else:
#         input= int(input)
#         if input<0:
#             raise Exception("x negatif değer olamaz")
#         Factorial(input)
# except Exception as ex:
#     print(ex)


# hoca

def faktoriyel (x):
    x = int (x)
    if x < 0:
        raise ValueError ('Negatif deger')
    result = 1
    for i in range (1, x+1):
        result *= i
    return result



for y in [5, 10, 20, -3, '10a']:
    try:
        z = faktoriyel(y)
        print(z)
        
        
    except ValueError as err:
        print (err)
        continue
    


