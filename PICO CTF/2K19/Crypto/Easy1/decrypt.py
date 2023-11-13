#!/usr/bin/env python3

"""
Solution for the PicoCTF 2K19 Cryptography Challenge - caesar.

Description: The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?

Solution: It is a simple rotational cipher.
cipher text = plaintext + key.  we can use this and table to find the plaintext 

Flag: picoCTF{CRYPTOISFUN}
"""

cipher = "UFJKXQZQUNB"
key = "SOLVECRYPTO"
flag = "picoCTF{"

table = open("table.txt", 'r').read()

# decrypting the cipher with key
for i in range(len(cipher)):
	val = (ord(cipher[i]) - ord(key[i]) + ord('A'))
	if val < 65:
		flag += chr(val + 26)
	else:
		flag += chr(val)

flag += "}"

print(flag)