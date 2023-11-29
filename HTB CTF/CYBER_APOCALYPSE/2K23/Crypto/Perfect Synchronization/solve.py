"""
This is the Write Up for Crypto Challenge of Cyber Apocalypse 2K23 CTF - Perfect Synchronization.

> Pratyush Prakhar (5#1NC#4N) - 03/20/20223

Description:
The challenge is about a secret message that is put in the `output.txt` file.
The method of encoding is presented in the `source.py` file.
This involves AES cryptography in CBC mode which is suspectable to frequency analysis attack as explained here - https://zachgrace.com/posts/attacking-ecb/


Solution:

Reverse engineer the message using known alphabets and common words using the frequency test .
"""

#!/usr/bin/env python3

from collections import Counter
from Crypto.Cipher import AES
from os import urandom


# AES ECB prone to 

def solve(data):
    new_data = [i.strip() for i in data]
    flag = {}

    resolve = {
        "d4dde50295a8c036709603b3c216e44d" : "{", # we get this from the flag format
        "25581e56ea570e8f68c9dab82f24f36e" : "}",
        "c98f7e77e918e98833b8fa19de4b1653" : "H",
        "d395fedae9dca912da1b1b50b0aca161" : "T",
        "cb20a26ba8411b2e0072e7438ed67e54" : "B",
        "00273fa04b9b836c553d876502e9a1e2" : "A", # by analysis of the data to get key words - THAT
        "d78843699ad962a2a7c513d193d27ab4" : "E", # by analysis of the data to get key words - THE
        "4ca1a8b8e8ca22b70d69ca257d79e5ed" : "S", # by analysis of the data and flag to get key words - BASE
        "4065e6b94c150f4137af46b752e25204" : "D", # by analysis of the data to get key words - BASED
        "9b9233be563be442bf2edf0e3e42848d" : "Y", # by analysis of the data to get key words - BY
        "b403c6f30eec7075d0643b5d4125de1b" : "N", # by analysis of the data to get key words - ANY
        "d3eae0ab73225a3d841241af5d8a0654" : "L", "98c50ceddda78b850757dc37c1c0814d" : "I", # by analysis of the data to get key words - ANALYSIS
        "0fbf645baa0ecce12ed52071a4ed0d1d" : "F", "ce2e2acd1155ac79105dcabcdb4fbbff" : "R", "9a2f91dbedaa39d9b53f8146c2301098" : "Q", "3ea6ab81fee5f5c718f48b86e8680732" : "U", "9e520d83ca02f81ab980ed7ff9a16526" : "C", # by analysis of the data to get key words - FREQUENCY
        "495c118c128a67d8a0f022e3f001775e" : "O", # by analysis of the data and flag to get key words - ON and SUBSTITUTION
        "a33f02cf75488a76efb91511a0111982" : "M", # by analysis of the data to get key words - COMBINATION
        "48654fae441fee7cd607d8cb90c1de44" : "P", # by analysis of the data and flag to get key words - SAMPLES, CIPHER, SIMPLE
        "97038e93767664edf41312c98285ba94" : "_", # by analysis of flag format
        "a952cfc1d886d6084113d5f3e13508f0" : " ",
    }
    fi = new_data.index("d4dde50295a8c036709603b3c216e44d") # only 1 occurrence each as in the flag format
    li = new_data.index("25581e56ea570e8f68c9dab82f24f36e")

    hash_flag = new_data[fi - 3: li+1]
    counter = Counter(hash_flag)
    # print(counter)
    out_msg = ""
    for char in new_data:
        if char in resolve.keys():
            out_msg += resolve[char]
        else:
            out_msg += "*"

    out_flag = ""
    for char in hash_flag:
        if char in resolve.keys():
            out_flag += resolve[char]
        else:
            out_flag += "*"
    print(out_msg)
    print(out_flag, fi, li) # flag is HTB{SIMPLE_SUBSTITUTION_CIPHER}



def main():
    data = open("./crypto_perfect_synchronization/output.txt", "r").readlines()

    solve(data)



if __name__ == "__main__":
    main()
