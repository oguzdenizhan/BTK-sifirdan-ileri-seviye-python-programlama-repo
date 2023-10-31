from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Twitter():
    def __init__(self,username,password):
        self.browserProfile= webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.browser.maximize_window()
        self.username =username
        self.password= password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        userInput= self.browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

        time.sleep(2)

        userInput.send_keys(self.username)
        btnGiris=self.browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]").click()
        time.sleep(2)

        passwordInput =self.browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        passwordInput.send_keys(password)
        time.sleep(3)
        btnPassword=self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
        time.sleep(2)

    def search(self,hashtag):
        searchInput = self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        result= []
        list = self.browser.find_elements(By.XPATH,"//article[@data-testid='tweet']/div/div/div[2]/div[2]/div[2]/div")
        time.sleep(2)
        print("count: "+str(len(list)))

        for i in list:
            result.append(i.text)
        loopCounter =0
        last_height =self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter>3:
                break
            self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")

            time.sleep(2)
            new_height= self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height==new_height:
                break
            
            last_height=new_height
            loopCounter+=1

            list = self.browser.find_elements(By.XPATH,"//article[@data-testid='tweet']/div/div/div[2]/div[2]/div[2]/div")
            time.sleep(2)
            print("count:  "+str(len(list)))

            for i in list:
                result.append(i.text)
        count =1   
        with open("tweets.txt","w",encoding="UTF-8") as file:
            for item in result:
                file.write(f"{count}- {item}\n")
                count+=1

#ekrana yazdırma

        # count=1
        # for item in result:
        #     print(f"{count}-{item}")
        #     count+=1
        #     print("*"*15)


twitter= Twitter(username,password)
twitter.signIn()
twitter.search("python")