#!/usr/bin/env python3

"""
Solution for the Pico-mini CTF 2K22 General Skill Challenge - HashingJobApp.

Description: If you want to hash with the best, beat this test!
nc saturn.picoctf.net 50561

Solution: nc provides with a script to supply back md5 hashes for the words. We can use this script to calculate and supply it back. We can also use pwn tools to interact directly and do it that way.

Flag: picoCTF{4ppl1c4710n_r3c31v3d_674c1de2}
"""

import hashlib

def generate_md5_hash(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

# Usage
def main():
    input_string = input("Input String to be hashed - ")
    print(f"MD5 Hash of '{input_string}' is {generate_md5_hash(input_string)}")


if __name__ == "__main__":
    main()