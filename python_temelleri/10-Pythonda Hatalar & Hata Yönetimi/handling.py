# error handling => hata yönetimi
# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)

# except ZeroDivisionError:
#     print("y için 0 girilemez.")

# except ValueError:
#     print("x ve y için sayısal değer giriniz.")

# except (ZeroDivisionError,ValueError):
#      print("x ve y için yanlış değer girdiniz.")

# except (ZeroDivisionError,ValueError)as e:
#     print("x ve y için yanlış değer girdiniz.")
#     print(e)



# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)


# except:
#     print("x ve y için yanlış değer girdiniz.")
    
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)


    except Exception as ex:
        print("x ve y için yanlış değer girdiniz: ",ex)

    else:
        break
    finally:
        print("try except sonlandı.")

