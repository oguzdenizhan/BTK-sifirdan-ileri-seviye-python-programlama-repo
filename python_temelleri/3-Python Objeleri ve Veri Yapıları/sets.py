fruits= {'apple','banana','orange'}

#print(fruits[0]) #indexlenemez

for x in fruits:
    print(x)
fruits.add('cherry')
fruits.update(['mango','grape','apple'])



print(fruits)

fruits.remove("mango")
fruits.discard("apple")

print(fruits)

fruits.pop() # listelerdeki gibi sondakini silmez index olmadığı için 
print(fruits)

fruits.clear()
print(fruits)
# myList=[1,2,4,5,1,3,2,4]
# print(myList)
# print(set(myList))