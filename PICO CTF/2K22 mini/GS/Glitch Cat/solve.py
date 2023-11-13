#!/usr/bin/env python3

"""
Solution for the Pico-mini CTF 2K22 General Skill Challenge - Glitch Cat.

Description: Our flag printing service has started glitching!
$ nc saturn.picoctf.net 49700

Solution: nc provides with an input which contains certain chr(hex) strings. So, let's convert them to get the flag.

Flag: picoCTF{gl17ch_m3_n07_a4392d2e}
"""

def main():
    inp_file = open("PICO CTF/2K22 mini/GS/Glitch Cat/nc_out.txt", "r")
    inp = inp_file.read()
    # print(inp)

    inp_list = inp.split("+")
    # print(inp_list)
    
    out = ""
    for word in inp_list:
        if "pico" in word or "}" in word:
            out += word.strip()[1:-1]
        else:
            out += chr(int(word.strip()[4:-1], base=16))
        # out += word.strip()
    
    print(out)

if __name__ == "__main__":
    main()