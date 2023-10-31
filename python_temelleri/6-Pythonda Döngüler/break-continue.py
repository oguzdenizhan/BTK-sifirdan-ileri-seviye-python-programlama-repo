# name= "Oğuzhan Denizhan"

# for letter in name:
#     # if(letter=="u"):
#     #     break
#     if(letter=="u"):
#         continue
#     print(letter)

# x=0
# while(x<5):
#     x+=1
#     if(x==2):
#         continue
#     print(x)
    

# 1 den 100 e kadar olan sayıların toplamı
x=0
toplam =0
while(x<=100):
    x+=1
    if(x%2==0):
        continue
    toplam+=x
    
print(f"Toplam: {toplam}")