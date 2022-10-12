import requests
from requests.structures import CaseInsensitiveDict
import json
import os
from dotenv import load_dotenv

load_dotenv()

headers = CaseInsensitiveDict()

headers["Content-Type"] = "application/json"
headers["Authorization"] = os.getenv("AUTH_TOKEN")

url = os.getenv("SAFE_KEY_URL")

def savekey(enc_priv,enc_pub,token):
    data = {"pri_key":enc_priv, "pub_key":enc_pub, "token":token}
    data = json.dumps(data, indent=2)
    res = requests.post(url, headers=headers, data=data)
    return res.status_code
