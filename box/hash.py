import time
from datetime import datetime
import hashlib
import math
import random

# generative hash
def hashes():
    dd = str(time.time()) + str(datetime.now())
    m = hashlib.sha256(dd.encode("UTF-8")).hexdigest()
    last_end = m[6:9]
    value =m[0:5] + m[-5:-1]
    rand = math.floor(random.random() * 78654456 + 956677754)
    hashess = "{0}{1}{2}".format(value, rand, last_end)
    final_hash = hashess[0:29]
    return final_hash
