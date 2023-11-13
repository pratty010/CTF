#!/usr/bin/env python3

"""
Solution for the Pico CTF 2k19 General Skill Challenge - Warmed Up.

Description: What is 0x3D (base 16) in decimal (base 10)?

Solution: Use int function with base=16

Flag: picoCTF{61}
"""

def main():
    inp = "3D"
    out = int(inp, base=16)

    print("Flag --> picoCTF{" + str(out) + "}")

if __name__ == "__main__":
    main()