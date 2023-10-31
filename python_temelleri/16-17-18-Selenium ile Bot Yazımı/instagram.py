from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
from selenium.webdriver.common.by  import By
import time
class Instagram:
    def __init__(self,username,password):
        self.browserProfile= webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.browser.maximize_window()

        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(6)
        usernameInput=self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput=self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(5)
    def getFollowers(self):

        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)
        self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click()

        time.sleep(3)

        dialog=self.browser.find_element(By.CSS_SELECTOR,'div[role=dialog]')
        followerCount=len(self.browser.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
        time.sleep(2)

        print(f"first count {followerCount}")

        action =webdriver.ActionChains(self.browser)

        max = int(self.browser.find_element(By.CSS_SELECTOR,'span[title="303"]').text)
        print(max)
        while True:
            dialog= self.browser.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div")
            dialog.click()
            
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            # scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
            # self.browser.execute_script(scroll_script)
            time.sleep(3)
            newCount = len(dialog.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
            newCount=  followerCount+newCount
            
            
            if followerCount <= max:
                print(f"updated count: {newCount}")
                followerCount+=newCount
                time.sleep(2)
            else:
                break
            followers = dialog.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")

        followerList= []
        for user in followers:
            link = user.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            followerList.append(link)
            
        with open("followers.txt", "w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")
        time.sleep(6)
    def followUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followButton = self.browser.find_element(By.TAG_NAME,"button")
        if followButton.text != "Following":
            followButton.click()
            time.sleep(3)
        else:
            print("Zaten Takiptesin")

    def unfollowUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followButton = self.browser.find_element(By.TAG_NAME,"button")
        if followButton.text == "Following":
            followButton.click()
            time.sleep(3)
            self.browser.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]").click()
        else:
            print("Zaten Takip etmiyorsun")


insta = Instagram(username,password)
insta.signIn()
insta.getFollowers()

# insta.followUser("kodfun")

# list = ["kod evreni", ""]
# for user in list:
#     insta.followUsero(user)
#     time. sleep(3)

# insta.unfollowUser("kodfun")


