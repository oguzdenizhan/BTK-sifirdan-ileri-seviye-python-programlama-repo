def sayHello(name="User"):
    return "Hello "+ name

msg=sayHello("Ada")
msg=sayHello("Aleyna")
print(msg)
msg=sayHello()
print(msg)


def total(num1,num2):
    return num1+num2
result=total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2023-dogumYili
oguzhanYas= yasHesapla(2000)
aleynaYas= yasHesapla(2011)
print(oguzhanYas,aleynaYas)

def EmekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRING: Dogum yiliniza göre emeklilige kac yil kaldi
    INPUT: Dogum yili, isim
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas=yasHesapla(dogumYili)
    emeklilik= 65-yas
    if emeklilik>0:
        print(f"Emekliliğe {emeklilik} yıl kaldı")
    else:
        print("zaten emeklisiniz")


EmekliligeKacYilKaldi(2000,"Oğuzhan")
EmekliligeKacYilKaldi(1944,"osman")
print(help(EmekliligeKacYilKaldi))
