##Brute Master - 250

####Я слышал, хакеры любят брутфорсить? 188.130.155.58:10002

Весь смысл таска в получении хеша, метода и части инпут строки с сервера и отправлении полноценной строки в ответ в течении 60 секунд. Всего 5 раундов.

Решение на python:

```# Welcome. You want to defuse the hashbomb, isn't it? So. You actually have to defuse 5 bombs. Are you ready?
# Level 1/5.
# Send us a string starting with k1dubcwrkxggztz4, ^[1-4a-z]{21}$, such that its sha1 hashsum equals to a4e422d35557b7d1d2bb6425acf1d98ee0d9b3d9. And... you have 60 seconds.

import hashlib
import itertools
import string
import re
from pwn import *
alphabet = string.lowercase + "1234"

r = remote("188.130.155.58", 10002)

reg = "with ([a-z1-4]{16}).*its (.*?) hashsum.*?to ([a-z0-9]+)"


def brute(start, method, hash):
    for i in itertools.product(alphabet, repeat=5):
        s = start + "".join(i)
        h = hashlib.new(method)
        h.update(s)
        if h.hexdigest() == hash:
            return s

r.recvline()
r.recvline()

for i in xrange(5):
    answer = r.recv()
    if answer.strip() == "level correct!":
        answer = r.recv()
    print i, " level", answer
    start, method, hash = re.search(reg,answer).groups()
    r.send(brute(start,method,hash))
    print r.recvline()
r.interactive()
