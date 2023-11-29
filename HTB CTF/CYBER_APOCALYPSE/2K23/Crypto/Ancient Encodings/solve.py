"""
This is the Write Up for Crypto Challenge of Cyber Apocalypse 2K23 CTF - Ancient Encodings.

> Pratyush Prakhar (5#1NC#4N) -03/20/20223

Description:
The challenge is about a secret message that is put in the `output.txt` file.
The method of encoding is presented in the `source.py` file.

Solution:

Reverse Engineered the encoding mechanism to get the plain .
"""

#!/usr/bin/env python3

from base64 import b64decode
from Crypto.Util.number import long_to_bytes

# Function to decode teh encoded flag.
def decode(flag):
    return b64decode(long_to_bytes(int(flag, 16))) # Unhex --> convert byte to long with padding --> Base64 decode.


def main():
    encoded_flag = open("./crypto_ancient_encodings/output.txt", "r").read().strip()    
    
    flag = decode(encoded_flag)
    print(flag)
    # HTB{411_7h3_3nc0d1n9_423_h323_70_574y}
    

if __name__ == "__main__":
    main()
