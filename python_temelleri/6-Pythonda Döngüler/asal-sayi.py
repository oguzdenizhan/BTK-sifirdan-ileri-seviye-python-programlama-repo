"""
Soru: Girilen bir sayinin asal olup olmadigina bulun.
** Asal Says 1 ve kendisi haric tam böleni olmayan sayilara denir.
"""
asalMi= True
girdi= int(input("Bir sayi giriniz: "))
if girdi==1:
    asalMi=False

for i in range(2,girdi):

    if(girdi%i==0):
        asalMi=False
        break    
if asalMi:
    print("Sayı Asaldır.")
else:
    print("Sayı Asal değildir.")
        