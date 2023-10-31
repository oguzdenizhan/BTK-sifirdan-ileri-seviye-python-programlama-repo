# def changeName(n):
#     n="ada"

# name = "aleyna"
# changeName(name)
# print(name)



# def change(n):
#     n[0]="istanbul"

# sehirler= ["ankara","izmir"]
# change(sehirler)
# print(sehirler)


# n=sehirler[:] #slicing
# n[0]= "istanbul"
# print(n)

# change(sehirler[:])
# print(sehirler)


# def add(a,b,c=0):
#     return sum((a,b,c))

# print(add(10,20))
# print(add(10,20,30))


def add(*params):
    print(type(params))
    print(params)
    print(params[0])
    return sum((params))

print(add(10,20))
print(add(10,20,30,50,60,7))

def displayUser(**args):
    print(type(args))
    for key,value in args.items():
        print("{} is {}".format(key,value))
    

displayUser(name="Ada",age=14,city="istanbul")
displayUser(name="Azra",age=23,city="kocaeli",phone="1659323")
displayUser(name="Yiğit",age=36,city="malatya",phone="456826",mail="yigit@gmail.com")


def function(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


function(10,20,30,40,50,key1="value 1",key2="value 2")
    

