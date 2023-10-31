import os
import datetime
result= dir(os)
result =os.name

#dizin değiştirme
# os.chdir("C:\\")
# os.chdir("..")
# os.chdir("../..")

#klasor olusturma
# os.mkdir("newdirector")
# os.makedirs("newdirector/yeniklasor")
# os.rename("newdirector","yeniklasor")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasor/yeniklasor")

#listeleme
# result = os.listdir()
# result = os.listdir("C:\\")
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

#etkin dizin öğrenme
# result =os.getcwd()


result= os.stat("date.py")
# result= result.st_size/1024
# result= datetime.datetime.fromtimestamp(result.st_ctime) #oluşturma tarihi
# result= datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
# result= datetime.datetime.fromtimestamp(result.st_mtime) # değişririlme tarihi

# os.system("notepad.exe")

#path
result =os.path.abspath("_os.py")
result =os.path.dirname("C:/Users/Oguzhan/Desktop/python_temelleri/_os.py")
result =os.path.dirname(os.path.abspath("_os.py"))
result= os.path.exists("_os.py")
result= os.path.exists("C:/Users/Oguzhan/Desktop/python_temellerii")
result = os.path.isdir("C:/Users/Oguzhan/Desktop/python_temelleri")
result = os.path.isfile("C:/Users/Oguzhan/Desktop/python_temelleri/_os.py")
result =os.path.join("c:\\","deneme","deneme1")
result =os.path.split("c:\\deneme")
result =os.path.splitext("_os.py")
# result=result[0]
result=result[1]




print(result)