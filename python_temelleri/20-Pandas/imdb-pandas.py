import pandas as pd
df= pd.read_csv("imdb.csv")
# 1 - Dosyada hakkindaki bilgiler.
result =df
result =df.columns
result =df.info
# 2- ilk 5 kaydı gösterin
result =df.head()

# 3- ilk 10 kaydı gösterin
result =df.head(10)
# 4- Son 5 kaydı gösterin
result =df.tail()
# 5- Son 10 kaydi gösterin
result =df.tail(10)

# 6- Sadece Movie_Title kolonunu alin.
result =df["Movie_Title"]

# 7 - Sadece Movie_Title kolonunu içeren ilkk 5 kayda alin.
result =df["Movie_Title"].head()

# 8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alin.
result =df[["Movie_Title","Rating"]].head()

# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alin.
result =df[["Movie_Title","Rating"]].tail(7)

# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alin.
# result =df[5:][["Movie_Title","Rating"]].head()
result =df[5:10][["Movie_Title","Rating"]]

#11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0
# ve üstünde olan kayitlardan ilk 50 tanesini aliniz.
result = df.query("Rating >= 8.0")[["Movie_Title","Rating"]].head(50)
result = df[df["Rating"] >=8.0][["Movie_Title","Rating"]].head(50)    
#12 - Yayın tarihi 2014 ile 2015 arasinda olan filmlerin isimlerini getiriniz.
result =df.query("YR_Released >=2014 & YR_Released <=2015")["Movie_Title"]
result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title","YR_Released"]]
#13 - Degerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı
#8 ile 9 arasinda olan filmleri listeleviniz
result =df.query("Num_Reviews >=100000| 8<= Rating <=9")["Movie_Title"]
result = df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title","Num_Reviews","Rating"]]

print(result)