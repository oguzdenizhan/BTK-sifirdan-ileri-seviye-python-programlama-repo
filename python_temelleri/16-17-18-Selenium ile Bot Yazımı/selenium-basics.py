from selenium import webdriver
import time


driver = webdriver.Chrome()

url = "https://github.com"
driver.get(url)

time .sleep(2)
driver.maximize_window()
# driver.save_screenshot("github.com-homepage.png")
url ="http://github.com/oguzdenizhan"
driver.get(url)
print(driver.title)

if "oguzdenizhan" in driver.title.lower():
    driver.save_screenshot("github-oguzdenizhan.png")


time .sleep(2)

driver.back()
# driver.forward()

time.sleep(2)
driver.close()


