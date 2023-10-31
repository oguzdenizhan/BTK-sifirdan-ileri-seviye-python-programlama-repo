# bankamatik Uygulaması

SadikHesap = {

    "ad":"Sadık Turan",
    "hesapNo":"13245687",
    "bakiye":3000,
    "ekHesap":2000

}

AliHesap = {

    "ad":"Ali Turan",
    "hesapNo":"4155245",
    "bakiye":2000,
    "ekHesap":1000

}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye']-=miktar
        print('paranızı alabilirsiniz')
        BakiyeSorgula(SadikHesap)
    else:
        toplam = hesap['bakiye']+hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı (e/h)")
            if ekHesapKullanimi== "e":

                ekHesapKullanilacakMiktar= miktar- hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz')
                BakiyeSorgula(SadikHesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("Uzgünüz bakiye yetersiz.")
            BakiyeSorgula(SadikHesap)

def BakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(SadikHesap,3000)
print("*"*100)
paraCek(SadikHesap,2000)

