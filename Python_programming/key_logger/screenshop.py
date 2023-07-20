import io
import pyautogui
from base64 import b64encode
import requests

API_KEY = ""
screenshot = pyautogui.screenshot("screenshot.png")
img_bytes = io.BytesIO()
screenshot.save(img_bytes, format="PNG")
img_bytes = img_bytes.getvalue()
img_encodeed = b64encode(img_bytes)

url = "https://api.imgbb.com/1/upload"
payload = {
    "key" : API_KEY,
    "image" : img_encodeed
}

res = requests.post(url, payload)
print(res.status_code)