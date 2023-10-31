import pymongo
from bson import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://oguzdeniz:My.123456.o@cluster0.c82wks2.mongodb.net/node-app?retryWrites=true&w=majority")

mydb= myclient["node-app"]
mycollection = mydb["products"]

#update_one

# result = mycollection.update_one(
#     {"name": "Samsung S5"},
#     {"$set": {
#         "name":"Iphone 5",
#     }}
# )

#update_many veri tabanındaki tüm samsung S7 leri değiştirir one da birden fazla olanların ilk bulduğunu değiştiryordu
# result = mycollection.update_many(
#     {"name": "Samsung S7"}, 
#     {"$set": {
#         "name":"Iphone 7",
#         "price":8000
#     }}
# )
# for i in mycollection.find():
#     print(i)

#dışarıda da tanımlayabiliriz
query = {"name": "Samsung S8"}
newQuery = {"$set": {
        "name":"Iphone 8",
        "price":8000
            }}
result = mycollection.update_many(query,newQuery)

print(f"{result.modified_count} adet kayıt güncellendi")
