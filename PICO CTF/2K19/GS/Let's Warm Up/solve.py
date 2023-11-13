#!/usr/bin/env python3

import binascii

"""
Solution for the Pico CTF 2k19 General Skill Challenge - Lets Warm Up.

Description: If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

Solution: Use binscii to convert hex to ascii.

Flag: picoCTF{p}
"""

def main():
    inp = "70"
    out = binascii.unhexlify(inp).decode()

    print("Flag --> picoCTF{" + out + "}")

if __name__ == "__main__":
    main()