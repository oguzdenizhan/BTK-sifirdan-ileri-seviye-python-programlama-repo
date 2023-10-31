import pymongo
from bson import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://oguzdeniz:My.123456.o@cluster0.c82wks2.mongodb.net/node-app?retryWrites=true&w=majority")

mydb= myclient["node-app"]
mycollection = mydb["products"]

# filter = {"name":"Samsung S5"}
# result = mycollection.find_one(filter)
# result = mycollection.find(filter)
# for i in result:
#     print(i)

# result = mycollection.find_one({"name":"Samsung S5"})
# result = mycollection.find_one({"_id":ObjectId("652aa7146c3dd08eac1a8184")})

# result = mycollection.find(
#     {
#         "name":{
#             "$in": ["Samsung S5","Samsung S6"] # ikisinden biri
#         }
#     }
# )

# result = mycollection.find(
#     {
#         "price":{
#             "$gt": 9000 #gt = greater than
#         }
#     }
# )

# result = mycollection.find(
#     {
#         "price":{
#             "$gte": 9000 #gte = greater than and equal

#         }
#     }
# )

# result = mycollection.find(
#     {
#         "price":{
#             "$eq": 9000 #equal  it means "price": 2000

#         }
#     }
# )

# result = mycollection.find(
#     {
#         "price":{
#             "$lte": 9000 #gte = less than and equal

#         }
#     }
# )

result = mycollection.find(
    {
        "name": {"$regex":"^S"} # s ile başlayan "regex" = regular expression
    }
)
for i in result:
    print(i)
# print(result)