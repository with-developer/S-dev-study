import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)

response.close()

soup = BeautifulSoup(response.content, "html.parser")
links = []
for a in soup.find_all("a"):
    href = a["href"]
    try:
        print(a["onclick"])
    except:
        pass
    if href.startswith("#") or href.startswith("@") or href.startswith("/") or href == "javascript:;":
        continue
    
#print(response.text)

