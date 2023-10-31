import requests

class Github:
    def __init__(self):
        self.api_url ="https://api.github.com"
        self.token = "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"
    
    def getUser(self,usarname):

        response = requests.get(self.api_url+"/users/"+usarname)
        return response.json()
    def getRepositories(self,usarname):

        response = requests.get(self.api_url+"/users/"+usarname+"/repos")
        return response.json()
    
    def createRepository(self,name):
        headers = {
            "Authorization": "token " + self.token
        }
        data = {
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
        response = requests.post(self.api_url + "/user/repos", headers=headers, json=data)

        return response.json()
github = Github()
while True:
    secim = input("1- Find User\n2- Get repositories\n3- Create Repository\n4- Exit\nSeçim: ")
    if secim == "4":
        break
    else:
        if secim=="1":
            usarname = input("usarname: ")
            result= github.getUser(usarname)
            print(f"name: {result['name']} public repos {result['public_repos']} followers: {result['followers']}")
        elif secim =="2":
            usarname = input("usarname: ")
            result= github.getRepositories(usarname)
            for repo in result:
                print(repo["name"])

        elif secim == "3":
            name = input("Repository name: ")
            result= github.createRepository(name)
            print(result)
        else:
            print("yanlış Seçim")


