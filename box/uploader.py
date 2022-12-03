import requests
from requests.structures import CaseInsensitiveDict
import json
import os
from dotenv import load_dotenv

load_dotenv()

headers = CaseInsensitiveDict()

headers["Content-Type"] = "multipart/form-data"
headers["Authorization"] = os.getenv("AUTH_TOKEN")

url = "http://127.0.0.1:9000/imagedeploy"

# function that communicate with internal ML api to get info
def read_image(image):
#file = {"image": open("apple.png", 'rb')}
    file = {"imagez": image}
    file = json.dumps(file, indent=2)
    res = requests.post(url, headers=headers, data=file)
    result = res.json()
    return res.status_code, result["result"]