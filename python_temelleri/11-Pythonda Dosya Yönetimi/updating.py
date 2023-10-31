# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())



# *****sayfa sonunda güncelleme ******
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nAda")

# *****sayfa basında güncelleme ******
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content= file.read()
#     content = "Efe\n"+ content
#     file.seek(0)
#     file.write(content)

# *****sayfa ortasına güncelleme ******
with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Nejla\n")
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())



