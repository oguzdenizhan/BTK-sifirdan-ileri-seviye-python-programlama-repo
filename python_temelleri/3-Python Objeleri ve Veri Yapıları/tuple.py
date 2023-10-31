list = [1,2,3]
tuple =(1, "iki", 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list = ["ali","veli"]
tuple = "damla", "ayşe", "ayşe"

list[0]= "ahmet"
print(list)
#tuple[0]="dilek"
#print(tuple) #ekledikten sonra değişiklik olmuyor listeden farkı

count=tuple.count("ayşe")
print(count)
index=tuple.index("ayşe")
print(index)

names = ("demet","emel","mahmut") + tuple
print(names)


