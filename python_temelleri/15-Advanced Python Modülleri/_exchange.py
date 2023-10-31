import requests
import json
#BEN
# result = requests.get("https://api.exchangerate.host/latest")

# result= json.loads(result.text)


# bozulan = input("bozulan döviz türü : ")
# alinan = input("alınan döviz türü : ")
# neKadar = input("Ne kadar bozdurmak istiyorsunuz : ")

# bozDeger=result["rates"][bozulan]
# alDeger=result["rates"][alinan]

# x= alDeger/bozDeger
# print(f"1 {bozulan} = {x} {alinan}")
# print(f"{1*int(neKadar)} {bozulan} = {x*int(neKadar)} {alinan}")


#HOCA
api_url= "https://api.exchangerate.host/latest?base="

bozulan_doviz = input("bozulan döviz türü : ")
alinan_doviz = input("alınan döviz türü : ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istoyorsun : "))

result=requests.get(api_url+bozulan_doviz)
result=json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*result["rates"][alinan_doviz],alinan_doviz))
