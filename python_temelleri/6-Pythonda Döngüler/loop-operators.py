#range
# for item in range(10):
#     print(item)

# for item in range(5,10):
#     print(item)
# for item in range(50,100,10):
#     print(item)

# print(list(range(5,100,10)))

#enumerate

# index=0
# greeting= 'Hello There'

# for letter in greeting:
#     # print(f'index {index} and letter {letter}')
#     print(f'index {index} and letter {greeting[index]}')
#     index+=1
 
# greeting= 'Hello There'
# # for item in enumerate(greeting):
# #     print(item)

# for index,letter in enumerate(greeting):
#     print(f'index {index} and letter {letter}')

#zip
list1= [1,2,3,4,5]
list2= ["a","b","c","d","e"]
list3= [10,20,30,40,50]
print(list(zip(list1,list2,list3)))

for item in list(zip(list1,list2,list3)):
    print(item)
for a,b,c in list(zip(list1,list2,list3)):
    print(a)