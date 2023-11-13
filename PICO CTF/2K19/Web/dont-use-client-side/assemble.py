#!/usr/bin/env python3

"""
Solution for the PicoCTF 2K19 Web Exploitation Challenge - dont-use-client-side.

Description: Can you break into this super secure portal?
https://jupiter.challenges.picoctf.org/problem/37821/ (link) or http://jupiter.challenges.picoctf.org:37821

Solution: Get the flag parts from the page source and then assemble it to get the flag.

Flag: picoCTF{no_clients_plz_1a3c89}
"""

import requests
from bs4 import BeautifulSoup


URL = "http://jupiter.challenges.picoctf.org:37821/"

page_source = requests.get(URL)
# print(page_source.text)

soup = BeautifulSoup(page_source.text, 'html.parser')

extracted_data = str(soup.find_all('script', {'type' : 'text/javascript'})[1]).split("\n")

useful_data = dict()

for word in extracted_data:
    if 'if (' in word.strip():
        print(word.strip().split("(")[2].split(")")[0], word.strip().split("(")[2].split(")")[1])
        
# Output from above loop.
# 0, split  == 'pico'
# split*6, split*7  == 'a3c8'
# split, split*2  == 'CTF{'
# split*4, split*5  == 'ts_p'
# split*3, split*4  == 'lien'
# split*5, split*6  == 'lz_1'
# split*2, split*3  == 'no_c'
# split*7, split*8  == '9}'

# Wish I knew regex better.
dic = {
0 : "pico",
6 : "a3c8",
1 : "CTF{",
4 : "ts_p",
3 : "lien",
5 : "lz_1",
2 : "no_c",
7 : "9}"
}

out = []
for i in range(8):
	out.append(dic[i])
print("".join(out))

