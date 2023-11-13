#!/usr/bin/env python3

"""
Solution for the PicoCTF 2K19 Cryptography Challenge - 13.

Description: Cryptography can be easy, do you know what ROT13 is?
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

Solution: Simple Rot13 decryption. I did it the python way. 

Flag: picoCTF{not_too_bad_of_a_problem}
"""

rot13_cipher = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

plain = ""
for ch in rot13_cipher:
	if ch.isupper():
		x = (ord(ch) + 13)
		plain += chr(x if x <= 90 else (x - 26)) 
	elif ch.islower():
		x = (ord(ch) + 13)
		plain += chr(x if x <= 122 else (x - 26))
	else:
		plain += ch

print(plain)