from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random, requests, os
from PIL import Image

def r_sleep():
    time.sleep(random.randint(3,5))

url = "https://comic.naver.com/webtoon/"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Referer" : "url"
}
comic_id = "769209"
browser = webdriver.Chrome()
no = 1
while(True):
    browser.get(url+"detail?titleId="+comic_id+"&no="+str(no))
    print("access",browser.current_url)
    browser.implicitly_wait(random.randint(3,5))
    r_sleep()

    image_files = []
    file_paths = []

    if url+"list?titleId="+comic_id == browser.current_url:
        print("finish")
        break

    for idx,img_element in enumerate(browser.find_elements(By.TAG_NAME, "img")):
        image_link = img_element.get_attribute("src")
        print(image_link)
        if "data:image/" in image_link or "/ssl.pstatic.net" in image_link or "naverwebtoon-phinf.pstatic.net" in image_link:
            continue
        response = requests.get(image_link, headers=headers)
        response.close()
        file_path = ".\\webtoon\\화산귀환_" + str(no) + "화_" + str(idx)+".png"
        fd = open(file_path, "wb")
        fd.write(response.content)
        fd.close()
        file_paths.append(file_path)

    img_list = []
    height = 0
    for file_path in file_paths:
        img = Image.open(file_path)
        print(file_path, img.width, img.height)
        if img.width != 690:
            continue
        
        img_list.append(img)
        height += img.height
    
    new_height = 0
    new_img = Image.new("RGB", (690, height), (256,256,256))
    for img in img_list:
        new_img.paste(img, box = (0, new_height))
        new_height += img.height
    
    new_img.save(".\\webtoon\\화산귀환_" + str(no) + ".png")
    new_img.close()
    print("Save Finish", ".\\webtoon\\화산귀환_" + str(no) + ".png")
    for file_path in file_paths:
        os.remove(file_path)
    no += 1
input()
    

#browser.find_elements(By.CLASS_NAME, "MyView-module__link_login___HpHMW")[0]