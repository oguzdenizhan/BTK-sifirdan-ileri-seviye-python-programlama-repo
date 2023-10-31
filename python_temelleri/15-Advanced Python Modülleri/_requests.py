import requests
import json
result =requests.get("https://jsonplaceholder.typicode.com/todos")


result= json.loads(result.text)

print(result[0]["title"])
print(result[0])

print(type(result))

# print(result)
for i in result:
    if i["userId"]==1:        
        print(i["title"])