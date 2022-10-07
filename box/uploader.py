import requests
from requests.structures import CaseInsensitiveDict
import json

headers = CaseInsensitiveDict()

headers["Content-Type"] = "multipart/form-data"

url = "http://127.0.0.1:4000/upload"

def read_image(image):
#file = {"image": open("apple.png", 'rb')}
    file = {"image": image}

    res = requests.post(url, headers=headers, data=file)
    print(res.json())