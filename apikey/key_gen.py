import time
from datetime import datetime
import hashlib
import math
import random
import os
from dotenv import load_dotenv

load_dotenv()

def key_encode(value, salt):
    dd = str(value) + str(salt)
    m = hashlib.sha256(dd.encode("UTF-8")).hexdigest()
    return m[0:42]

def hash(key):
    b_key = "Bearer {0}".format(key)
    n = hashlib.sha256(b_key.encode("UTF-8")).hexdigest()
    return n


def all_key(email):
    pk_salt = os.getenv("PK_SALT")
    sk_salt = os.getenv("SK_SALT")
    dd = str(time.time()) + str(datetime.now())
    
    rand = math.floor(random.random() * 78654456 + 956677754)
    hashess = "{0}{1}{2}".format(rand, email, dd)
    pk_key = "pk_live_{0}".format(key_encode(hashess,pk_salt))
    sk_key = "sk_live_{0}".format(key_encode(hashess,sk_salt))
    enc_pk_key = hash(pk_key)
    enc_sk_key = hash(sk_key)
    
    return pk_key,sk_key, enc_pk_key, enc_sk_key
