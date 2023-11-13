#!/usr/bin/env python3

"""
Solution for the Pico CTF 2k19 General Skill Challenge - Lets Warm Up.

Description: Can you convert the number 42 (base 10) to binary (base 2)?

Solution: Use bin() from int.

Flag: picoCTF{101010}
"""

def main():
    inp = 42
    out = bin(inp)

    print("Flag --> picoCTF{" + out[2:] + "}")

if __name__ == "__main__":
    main()