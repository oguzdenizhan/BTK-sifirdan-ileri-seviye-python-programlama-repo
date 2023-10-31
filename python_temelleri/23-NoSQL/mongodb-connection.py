# jimepah857@dixiser.com
import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017") #yerel
myclient = pymongo.MongoClient("mongodb+srv://oguzdeniz:My.123456.o@cluster0.c82wks2.mongodb.net/node-app?retryWrites=true&w=majority")

mydb= myclient["node-app"]

# print(myclient.list_databases_names()) # artık kullanımı önerilmiyor onun yerine
database_names = [db["name"] for db in myclient.list_databases()]

print(database_names)