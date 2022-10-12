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

def putkey(old_priv,enc_priv,enc_pub):
    data = {"oldpriv_key": old_priv, 
            "enc_priv_key": enc_priv,
            "enc_pub_key":enc_pub}
    data = json.dumps(data, indent=2)
    res = requests.put(url, headers=headers, data=data)
    return (res.status_code)
