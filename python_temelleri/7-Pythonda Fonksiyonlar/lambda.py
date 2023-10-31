#1
# def square(num): return num**2

# numbers= [1,3,5,9]
# result = list(map(square,numbers))
# print(result)

# for item in map(square,numbers):
#     print(item)

#2
# def square(num): return num**2

# numbers= [1,3,5,9]
# result = list(map(lambda num: num **2 ,numbers))
# print(result)

# square= lambda num: num **2
# numbers= [1,3,5,9]
# result = list(map(square ,numbers))
# print(result)

# result=square(3)
# print(result)


numbers= [1,3,5,9,10,14]
def check_even(num): return num%2==0

# result = list(map(check_even,numbers))

# result = list(filter(check_even,numbers))
# result = list(filter(lambda num: num%2==0,numbers))
check_even = lambda num: num%2==0
result = list(filter(check_even,numbers))

result = check_even(numbers[2])




print(result)
