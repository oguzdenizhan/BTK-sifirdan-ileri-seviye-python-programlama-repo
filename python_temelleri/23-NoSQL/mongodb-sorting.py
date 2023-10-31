import pymongo
from bson import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://oguzdeniz:My.123456.o@cluster0.c82wks2.mongodb.net/node-app?retryWrites=true&w=majority")

mydb= myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort("name")
result = mycollection.find().sort("name",-1) # 1 artan şekilde sırala -1 azalan
result = mycollection.find().sort("price",-1)
result = mycollection.find().sort([("name",1),("price",-1)])


for i in result:
    print(i)