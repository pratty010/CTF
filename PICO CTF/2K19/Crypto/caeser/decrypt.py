#!/usr/bin/env python3 

"""
Solution for the PicoCTF 2K19 Cryptography Challenge - caesar.

Description: Decrypt this message - ciphertext.

Solution: Simple Caesar's cipher. But the rotation matters.

Flag: picoCTF{crossingtherubiconzaqjsscr}
"""

inp = open("ciphertext", 'r').read()

cipher = inp[inp.find("{") + 1 : inp.find("}")]

# Print all possible plaintext for shifts 1-25
for i in range(1, 26):
	plain = ""
	for alpha in cipher:
		if (ord(alpha) - i) < 97 :
			plain += chr(ord(alpha) - i + 26)
		else:
			plain += chr(ord(alpha) - i)
	print("{} : {}".format(i, plain))  
