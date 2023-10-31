#İdentity Operator: Is
x = y= [1,2,3]
z= [1,2,3]

# #değer karşılaştırma
# print(x==y)
# print(x==z)
# #adres karşılaştırma
# print(x is y)
# print(x is z)

#ornek
x= [1,2,3]
y= [2,4]


del x[2]
y[1]= 1
y.reverse()

# print(x==y)
# print(x is y)

#Membership Operator: In

x= ["apple","banana"]
print("apple"in x)

name= "Oğuzhan"
print("a"in name)
print("a"not in name)