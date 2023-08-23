from stem.control import Controller
from stem import Signal
import time
import requests

country_code = 'US'

proxies = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}
# http://ip-api.com/line 링크는 현재 접속한 위치를 보여줌
ip_response = requests.get("http://ip-api.com/line", proxies= proxies)
ip_response.close()
for line in ip_response.content.decode("utf-8").split("\n"):
    print(line)
# 9151 포트를 이용해서 ip 변경 진행
controller = Controller.from_port(port= 9151)
controller.authenticate(password="####")
# 원하는 국가의 출구 노드로 설정
controller.set_conf('ExitNodes', '{%s}' % country_code)
# Signal.NEWNYM을 출력해보자
#print(Signal.NEWNYM)
controller.signal(Signal.NEWNYM)
time.sleep(5) #5 sec
# 변경된 IP 다시 출력됨
ip_response = requests.get("http://ip-api.com/line", proxies= proxies)
ip_response.close()
for line in ip_response.content.decode("utf-8").split("\n"):
    print(line)