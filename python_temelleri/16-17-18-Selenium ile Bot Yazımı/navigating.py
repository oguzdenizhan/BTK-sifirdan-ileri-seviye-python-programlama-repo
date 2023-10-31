from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()

url ="http://github.com"

driver.get(url)
driver.maximize_window()
time.sleep(3)

searchInput = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button")
time.sleep(3)
searchInput.send_keys(Keys.ENTER)
time.sleep(3)
searchInput = driver.find_element("id","query-builder-test")
time.sleep(3)
searchInput.send_keys("python")

time.sleep(3)

searchInput.send_keys(Keys.ENTER)
time.sleep(3)

# result = driver.page_source
# print(result)

# result = driver.find_elements(By.CSS_SELECTOR, '.Box-sc-g0xbh4-0.kXssRI h3 a span')
# for element in result:
#     print(element.text)
# driver.close()

