#!/usr/bin/env python3

"""
Solution for the Pico-mini CTF 2K22 General Skill Challenge - convertme.py.

Description: Run the Python script and convert the given number from decimal to binary to get the flag.

Solution: Reuse script to convert int to bin format.

Flag: picoCTF{4ll_y0ur_b4535_9c3b7d4d}
"""

def main():
    inp = input("Please provide decimal number here - ")
    out = bin(int(inp))

    print("Converted binary output - " + out[2:])

if __name__ == "__main__":
    main()