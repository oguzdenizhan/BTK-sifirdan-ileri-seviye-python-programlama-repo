#Yöntem 1

# import math
import math as islem
# value = dir(math)
# value = help(math)
# value = help(math.factorial)

# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5.9)
# value = math.ceil(5.9)

# value = islem.factorial(5)

#Yöntem 2
# from math import *


from math import factorial,sqrt,ceil
def sqrt(x): # hangisi en son tanımlanırsa onu kullanır importtan önce tanımlasaydık bu metotu kullanmazdı
    print("x: "+str(x))

value = factorial(5)
value = ceil(9.8)
value = sqrt(9)

print(value)