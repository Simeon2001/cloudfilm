import requests
from requests.structures import CaseInsensitiveDict
import json
import os
from dotenv import load_dotenv

load_dotenv()

headers = CaseInsensitiveDict()

headers["Content-Type"] = "application/json"

url = os.getenv("SAFE_KEY_URL")

def savekey(enc_priv,enc_pub,token):
    data = {"pri_key":enc_priv, "pub_key":enc_pub, "token":token}
    res = requests.post(url, headers=headers, data=data)
    print(res.json())