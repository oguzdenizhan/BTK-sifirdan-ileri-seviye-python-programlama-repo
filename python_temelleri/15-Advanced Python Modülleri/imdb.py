import requests
from bs4 import BeautifulSoup

url= "https://www.imdb.com/chart/top/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

html = requests.get(url, headers=headers).content



soup = BeautifulSoup(html,"html.parser")

list = soup.find("ul", {"class":"ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base"}).find_all("li",limit=50)

count =0
for tr in list:
    title= tr.find("td",{"class":"titleColumn"}).fin("a").text
    year= tr.find("td",{"class":"titleColumn"}).fin("span").text.strip("()")
    rating= tr.find("td",{"class":"titleColumn imdbRating"}).fin("strpng")
    count +=1
    print(f"{count}- film: {title.ljust(50)} yıl: {year} değerlendirme: {rating}")





