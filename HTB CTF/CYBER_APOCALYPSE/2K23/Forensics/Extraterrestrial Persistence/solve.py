"""
This is the Write Up for Forensics Challenge of Cyber Apocalypse 2K23 CTF - Extraterrestrial Persistence.

> Pratyush Prakhar (5#1NC#4N) - 03/20/20223

Description:
The challenge is about shell code file `persistence.sh`.
It consist of a secret message being pushed to systemd file.


Solution:

Let's decode the string and find out what does it exactly say.
"""

#!/usr/bin/env python3

from base64 import b64decode

def solve(data):
    base_str = "W1VuaXRdCkRlc2NyaXB0aW9uPUhUQnt0aDNzM180bDEzblNfNHIzX3MwMDAwMF9iNHMxY30KQWZ0ZXI9bmV0d29yay50YXJnZXQgbmV0d29yay1vbmxpbmUudGFyZ2V0CgpbU2VydmljZV0KVHlwZT1vbmVzaG90ClJlbWFpbkFmdGVyRXhpdD15ZXMKCkV4ZWNTdGFydD0vdXNyL2xvY2FsL2Jpbi9zZXJ2aWNlCkV4ZWNTdG9wPS91c3IvbG9jYWwvYmluL3NlcnZpY2UKCltJbnN0YWxsXQpXYW50ZWRCeT1tdWx0aS11c2VyLnRhcmdldA=="

    out = b64decode(base_str).decode("utf-8")

    return out

def main():
    file = open("./persistence.sh", "r")
    b_str = file.read()
    data = solve(b_str)

    print(data) # flag is in the output --> HTB{th3s3_4l13nS_4r3_s00000_b4s1c}

    file.close()

if __name__ == "__main__":
    main()