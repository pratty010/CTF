"""
Solution for the PicoCTF 2K19 Cryptography Challenge - The Numbers.

Description: The numbers...(in the picture) what do they mean?

Solution: The numbers denote the alphabetical characters in order with A = 1, B = 2, yada, yada. Let's create a simple substitution script.

Flag: PICOCTF{THENUMBERSMASON}
"""

#!/usr/bin/env python3

import string

input = [16, 9, 3, 15, 3, 20, 6, 0, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13,1, 19, 15 ,14, -1]
alpha = list(string.ascii_uppercase)
dic = {}

for i in range(1, 27):
	dic[i] = alpha[i - 1]
dic[0] = "{"
dic[-1] = "}"

flag = []
for inp in input:
	flag.append(dic[inp])

print("".join(flag))
