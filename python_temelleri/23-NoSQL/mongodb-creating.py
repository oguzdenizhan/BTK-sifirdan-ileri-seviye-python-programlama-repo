import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://oguzdeniz:My.123456.o@cluster0.c82wks2.mongodb.net/node-app?retryWrites=true&w=majority")

mydb= myclient["node-app"]

mycollection = mydb["products"]

# print(mydb.list_collection_names())

# product = {"name":"Samsung S5","price":5000}

# result=mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id)

# {"_id":1,name":"Samsung S6","price":6000} şeklinde id de vereblilirdik

# productList= [
#     {"name":"Samsung S6","price":6000},
#     {"name":"Samsung S7","price":7000},
#     {"name":"Samsung S8","price":8000},
#     {"name":"Samsung S9","price":9000},
#     {"name":"Samsung S10","price":10000},
#     {"name":"Samsung S11","price":11000}

# ]

productList= [
    {"name":"Samsung S6","price":6000,"description":"iyi telefon"},
    {"name":"Samsung S7","price":7000,"category":["telefon","elekronik"]}
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)