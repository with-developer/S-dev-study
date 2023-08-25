import requests

proxies = {
    "http":"socks5://127.0.0.1:9150",
    "https":"socks5://127.0.0.1:9150"
}

response = requests.get("http://ip-api.com/line", proxies=proxies)
print(response.text)