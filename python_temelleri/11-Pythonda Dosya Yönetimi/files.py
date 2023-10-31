# Dosya açmak ve olusturmak için open() fonksiyonu kullanalir.
# Kullanimi: open(dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => dosyayı hangi amaçla açtigimizi belirtir.

# "w": (Write) yazma modu. Dosyayı konumda olusturur.
#** Dosyayı konumda oluşturur.
#** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w")
# file = open("C:/users/Oguzhan/desktop/newfile.txt","w")

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Sadık Turan")
# file.close()
#"a": (Append) ekleme. Dosya konumda yoksa olusturur.
# file = open("newfile.txt","a",encoding="utf-8")
# file.close()
# x": (Create) olusturma. Dosya zaten varsa hata verir.
file = open("newfile2.txt","x",encoding="utf-8")

# r": (Read) okuma. varsayilan. dosya konumda yoksa hata verir.