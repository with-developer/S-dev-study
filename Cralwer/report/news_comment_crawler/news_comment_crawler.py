from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from konlpy.tag import *
import os
os.environ["JAVA_HOME"]  = "C:\\Users\\user\\AppData\\Local\\Programs\\BurpSuiteCommunity\\jre\\bin\\server"
kkma = Kkma()
browser = webdriver.Chrome()
browser.get("https://n.news.naver.com/article/comment/088/0000828242")
browser.implicitly_wait(5)
time.sleep(3)
while True:
    try:
        btn_more = browser.find_element(By.CLASS_NAME, "u_cbox_btn_more")
        if not btn_more:
            break
        btn_more.send_keys(Keys.END)
        btn_more.click()
        time.sleep(3)        
    except:
        break

for c_box_area in browser.find_elements(By.CLASS_NAME, "u_cbox_area"):
    try:
        nick = c_box_area.find_element(By.CLASS_NAME, "u_cbox_nick")
        date = c_box_area.find_element(By.CLASS_NAME, "u_cbox_date")        
        try:
            contents = c_box_area.find_element(By.CLASS_NAME, "u_cbox_contents")
        except:
            contents = c_box_area.find_element(By.CLASS_NAME, "u_cbox_btn_totalcomment")
            
        recomm = c_box_area.find_element(By.CLASS_NAME, "u_cbox_cnt_recomm")
        unrecomm = c_box_area.find_element(By.CLASS_NAME, "u_cbox_cnt_unrecomm")
        #print(kkma.pos(contents.text))
        print(nick.text, date.text, contents.text, recomm.text, unrecomm.text)
        btn = c_box_area.find_element(By.CLASS_NAME, "u_cbox_btn_totalcomment")
        btn.click()
        time.sleep(7)
        userpage = browser.find_element(By.CLASS_NAME, "u_cbox_layer_userpage")
        close_btn = userpage.find_element(By.CLASS_NAME, "u_cbox_userpage_closebtn")
        close_btn.click()
        
    except:
        continue
'''
for btn in browser.find_elements(By.CLASS_NAME, "u_cbox_btn_totalcomment"):
    try:
        btn.click()
        browser.implicitly_wait(5)        
        webdriver.ActionChains(browser).key_down(Keys.ESCAPE).perform()
    except:
        pass
'''
input()
    
    