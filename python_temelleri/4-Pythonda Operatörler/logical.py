x=6
hak =0
devam= "e"
# result =5<x<10
# print(result)

#and  t t -> t
# result= (x>5) and (x<10)
# result= (hak>0) and (devam=="e")
# print(result)

#or   t f -> t
# result= (x>0) or (x % 2 == 0)
# print(result)
#not  t -> f
# result= not(x<0)
# print(result)

# x, 5-10 arasinda olan bir çift say mi?
result= ((x>5) and (x<10)) and (x % 2 == 0)
print(result)