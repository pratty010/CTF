"""
Solution for the Pico-mini CTF 2K22 General Skill Challenge - PW Crack 1.

Description: Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag in the same directory too.

Solution: On going through the script, the level_1_pw_check() reveals that password to be supplied is 8713. We can supply that to get the flag.

Flag: picoCTF{545h_r1ng1ng_1b2fd683}
"""

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open('level1.flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
