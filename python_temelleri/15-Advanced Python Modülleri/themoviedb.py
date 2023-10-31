# themoviedb.org =› film ve dizi arsivi
# themoviedb' nin sundugu apiyi ugulamanizda kullaniniz.
# Anahtar kelimeye göre arama
# En popüler film listesi
# Vizyondaki film listesi


import requests

class theMovieDb:
    def __init__(self):
        self.api_url ="https://api.themoviedb.org/3"
        self.api_key = "9b1127571ce823a004fbf2c7033b32f1"
    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    def getSearchResult(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()
movieApi = theMovieDb()
while True:
    secim = input("1- popular Movies\n2-Search Movies\n3- Exit\n Secim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])
        if secim == "2":
            keyword = input("keyword: ")
            movies = movieApi.getSearchResult(keyword)
            for movie in movies["results"]:
                print(movie["name"])




