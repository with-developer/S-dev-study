import requests

url = "https://search.shopping.naver.com/api/product-zzim/add"

headers= {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "application/json",
    "Sbth": "",
    "Cookie": "",
    "Referer": "https://search.shopping.naver.com/search/all?frm=NVSCTAB&origQuery=%ED%8C%8C%EB%A6%AC%EC%B1%84&pagingIndex=2000&pagingSize=40&productSet=total&query=%ED%8C%8C%EB%A6%AC%EC%B1%84&sort=rel&timestamp=&viewType=list"
}
body={"nvMid":"32147867542","isAd":False,"tr":"slsl","chpid":"","isHotdeal":False,"isAdult":False,"isBook":False}

response = requests.post(url, json=body, headers=headers)

print(response.text)
