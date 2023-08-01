from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/hm_son7/")
browser.implicitly_wait(random.randint(3,5))
time.sleep(random.randint(3,5))
input()
current_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    time.sleep(5)
    browser.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    height = browser.execute_script("return document.body.scrollHeight")
    print(current_height, height)
    if current_height == height:
        break
    current_height = height
input()
    
    

#browser.find_elements(By.CLASS_NAME, "MyView-module__link_login___HpHMW")[0]