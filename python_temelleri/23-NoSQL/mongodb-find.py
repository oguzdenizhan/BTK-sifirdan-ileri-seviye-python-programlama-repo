import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://oguzdeniz:My.123456.o@cluster0.c82wks2.mongodb.net/node-app?retryWrites=true&w=majority")

mydb= myclient["node-app"]
mycollection = mydb["products"]

# result= mycollection.find_one()

# for i in mycollection.find(): # select * gibi düşünebiliriz
#     print(i)

for i in mycollection.find({},{"_id":0,"name":1,"price":1}): # görmek istersek 1 istemezsek 0
    print(i)
for i in mycollection.find({},{"_id":0,"name":0}): # sadece istemediklerimizi de yazabiliriz 
    print(i)

# print(result)