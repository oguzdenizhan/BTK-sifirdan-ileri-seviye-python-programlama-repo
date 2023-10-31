"""
ogrenciler = {

    "120":{
        "ad":"Ali",
        "soyad":"Yılmaz",
        "telefon":"532 000 00 01"

    },
    "125":{
        "ad":"Can",
        "soyad":"Korkmaz",
        "telefon":"532 000 00 02"

    },

    "128":{
        "ad":"Volkan",
        "soyad":"Yükselen",
        "telefon":"532 000 00 03"

    }
}

1 Bilgileri verilen öğrencileri dictionary de sakla
2 Öğrenci numarasını alıp öğrenci bilgisini göster
"""

#1


# no="120"
# ad="Ali"
# soyad ="Yılmaz"
# Tel ="532 000 00 01"

# no2="125"
# ad2="Can"
# soyad2 ="Korkmaz"
# Tel2 ="532 000 00 02"

# no3="128"
# ad3="Volkan"
# soyad3 ="Yükselen"
# Tel3 ="532 000 00 03"


# ogrenciler = {
#     no:{
#         "ad":ad,
#         "soyad":soyad,
#         "telefon":Tel
#     },

#         no2:{
#         "ad":ad2,
#         "soyad":soyad2,
#         "telefon":Tel2
#     },
#         no3:{
#         "ad":ad3,
#         "soyad":soyad3,
#         "telefon":Tel3
#     }
# }


# #2
# print(ogrenciler[no])
# print(ogrenciler["125"])
ogrenciler ={}

number = input("Öğrenci no: ")
name = input("Öğrenci ad: ")
lastname = input("Öğrenci soyad: ")
phone = input("Öğrenci telefon: ")

# ogrenciler[number]={
#     "ad":name,
#     "soyad":lastname,
#     "telefon":phone
# }

ogrenciler.update({
    number:{
    "ad":name,
    "soyad":lastname,
    "telefon":phone

    }
})

number = input("Öğrenci no: ")
name = input("Öğrenci ad: ")
lastname = input("Öğrenci soyad: ")
phone = input("Öğrenci telefon: ")

ogrenciler.update({
    number:{
    "ad":name,
    "soyad":lastname,
    "telefon":phone

    }
})

number = input("Öğrenci no: ")
name = input("Öğrenci ad: ")
lastname = input("Öğrenci soyad: ")
phone = input("Öğrenci telefon: ")

ogrenciler.update({
    number:{
    "ad":name,
    "soyad":lastname,
    "telefon":phone

    }
}
)

# print(ogrenciler)
print("*"*50)
ogrNo= input("Öğrenci No")
ogrenci=ogrenciler[ogrNo]
print(f" Aradığınız {ogrNo} numaralı öğrencinin adı {ogrenci['ad']} soyadı {ogrenci['soyad']} ve telefonu {ogrenci['telefon']}")