from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random
import openpyxl
import os
from konlpy.tag import *
kkma = Kkma()
#os.environ["JAVA_HOME"] = "C:\\Users\\user\\AppData\\Local\\Programs\\BurpSuiteCommunity\\jre\\bin"

def r_sleep():
    time.sleep(random.randint(3,5))

url = "https://n.news.naver.com/mnews/article/comment/001/0014105194/"

browser = webdriver.Chrome()
browser.get(url)
print("access",browser.current_url)
browser.implicitly_wait(random.randint(3,5))
r_sleep()

while True:
    try:
        btn_more = browser.find_element(By.CLASS_NAME, "u_cbox_btn_more")
        if not btn_more:
            break
        btn_more.send_keys(Keys.END)
        btn_more.click()
        r_sleep()
        break #TODO: DELETE this line
    except:
        break

comment_dict = {}
for c_box_area in browser.find_elements(By.CLASS_NAME, "u_cbox_area"):
    
    nick = c_box_area.find_element(By.CLASS_NAME, "u_cbox_nick")
    #print(nick.text)
    try:
        comment = c_box_area.find_element(By.CLASS_NAME, "u_cbox_contents")
        print(kkma.pos(comment.text))
        #print(comment.text)
        good = c_box_area.find_element(By.CLASS_NAME, "u_cbox_cnt_recomm")
        #print(good.text)
        bad = c_box_area.find_element(By.CLASS_NAME, "u_cbox_cnt_unrecomm")
        #print(bad.text)

        comment_dict[nick.text] = [comment.text, good.text, bad.text]

    except:
        continue
    
#print(comment_dict)
for key, value in comment_dict.items():
    print(key)
    print(value)

# book = openpyxl.Workbook()
# sheet = book.active
# sheet.append(["계정명","댓글내용","좋아요","싫어요"])
# for key, value in comment_dict.items():
#     sheet.append([key, value[0],value[1],value[2]])

# book.save("result.xlsx")
# book.close()

input()
    