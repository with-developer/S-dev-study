from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random, time
import pyperclip

user_id = ''
user_pw = ''

def sleep():
    time.sleep(random.randint(1,2))

browser = webdriver.Chrome()
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
browser.implicitly_wait(random.randint(3,5))

sleep()
input_id_box = browser.find_element(By.ID, "id")

pyperclip.copy(user_id)
input_id_box.send_keys(Keys.CONTROL, 'v')

sleep()
input_pw_box = browser.find_element(By.NAME, "pw")

pyperclip.copy(user_pw)
input_pw_box.send_keys(Keys.CONTROL, 'v')

sleep()
submit_button_box = browser.find_element(By.ID, "log.login")
submit_button_box.click()

cookie_string = ""
cookies_list = browser.get_cookies()
for cookie in cookies_list[:-1]:
    cookie_string = cookie_string + cookie["name"] +"="+cookie["value"] + "; "
cookie_string = cookie_string + cookies_list[-1]["name"] + "=" + cookies_list[-1]["value"]
print(browser.current_url)
print(cookie_string)


input()
browser.close()