import pymongo
from bson import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://oguzdeniz:My.123456.o@cluster0.c82wks2.mongodb.net/node-app?retryWrites=true&w=majority")

mydb= myclient["node-app"]
mycollection = mydb["products"]

for i in  mycollection.find():
    print(i)

print("*"*50)

# result= mycollection.delete_one({"name":"Samsung S9"})

# for i in  mycollection.find():
#     print(i)

# result= mycollection.delete_one({"name":"Samsung S6"}) #veritabanında 2 tane ama 1 tanesini siler
# for i in  mycollection.find():
#     print(i)


#delete_many şarta uyanların hepsini siler

# result= mycollection.delete_many({"name":{"$regex":"^S"}}) 
result= mycollection.delete_many({}) #bütün kayıtları sil
print(f"{result.deleted_count} tane kayıt silindi")

for i in  mycollection.find():
    print(i)