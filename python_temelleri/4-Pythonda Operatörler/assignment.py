# x=5
# y= 10
# z=15

x,y,z=5,10,15

# x,y =y,x

x += 5 # x = x + 5
x -= 5 # x = x - 5
x *= 5 # x = x * 5
x /= 5 # x = x / 5
x %=5 
y //=5 #tam bölme
y**=z

#print(x,y,z)

values = 1,2,3
print(type(values))
x,y,z=values
print(x,y,z)


values = 1,2,3,4,5
x,y,*z=values
print(x,y,z)
print(x,y,z[1])
