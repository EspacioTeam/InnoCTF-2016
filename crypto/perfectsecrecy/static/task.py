#!/bin/python3

with open("flag.txt", "rb") as flag:
	key = flag.read()

with open("text.txt",  "rb") as r, \
     open("encrypted", "wb") as w:
	
	text = r.read()
	k = 0
	for byte in text:
		letter = byte ^ key[k]
		k = (k + 1) % 20
		w.write(chr(letter).encode("utf-8"))
