# key - value

#44 => Malatya 34 => İstanbul

# sehirler= ["Malatya","İstanbul"]
# plakalar = [44,34]

# print(plakalar[sehirler.index("Malatya")])
# print(plakalar[sehirler.index("İstanbul")])

# print(plakalar["Malatya"]) => 44
# print(plakalar["İstanbul"]) => 44

# plakalar= {"Malatya" : 44, "İstanbul" : 34}
# print(plakalar["Malatya"])
# print(plakalar["İstanbul"]) 

# plakalar["Ankara"]= 6
# plakalar["Malatya"] ="new value"
# print(plakalar)


users = {
    "oğuzhandenizhan":{
        "age":23,
        'roles':['users'],
        "email":"oguz@gmail.com",
        "address": "İstanbul",
        "phone": "1323133"


    },
    "aleynadenizhan" :{
        "age":12,
        'roles':['admin','users'],
        "email":"aleyna@gmail.com",
        "address": "İstanbul",
        "phone": "4676646"
    }
}

print(users["aleynadenizhan"])
print(users["aleynadenizhan"]["age"])
print(users["aleynadenizhan"]["email"])
print(users["aleynadenizhan"]["address"])

print(users["aleynadenizhan"]["roles"][0])


