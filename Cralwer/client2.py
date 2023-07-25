# allow_redirects False �� �곕Ⅸ http �붿껌 �ㅻ뜑 蹂��� �뚯븙
# requests 紐⑤뱢 �꾪룷��
import requests
# warnings �먮윭 �쒖뼱瑜� �꾪븳 urllib3 �꾪룷��
import urllib3
# warnings �먮윭 disable
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# �щ＼ 釉뚮씪�곗� �ㅼ젙
headers ={
    "User-Agent" : "Mozilla/5.01 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


# �쒕쾭 �묐떟肄붾뱶媛� 302 �쇱떆 由щ떎�대젆�� �먮룞 �댁젣
response = requests.get("http://www.naver.com", headers=headers, allow_redirects=False)
if response.status_code == 302:
    print("check")
    
    headers["Referer"] = "http://www.naver.com"
    
    response2 = requests.get(response.headers["Location"], headers=headers, allow_redirects=False, verify=False)
    print(response2.status_code)
    print(response.text)

#response = requests.get("http://www.naver.com", headers=headers, allow_redirects=True)