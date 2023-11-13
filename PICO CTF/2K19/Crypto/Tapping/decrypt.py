#!/usr/bin/env python3

"""
Solution for the PicoCTF 2K19 Cryptography Challenge - Tapping.

Description: Theres tapping coming in from the wires.
What's it saying nc jupiter.challenges.picoctf.org 21610.

Solution: The output message from nc listener is morse code. Let's create a decryption for it.

Flag: PICOCTF{M0RS3C0D31SFUN3902019519}
"""

morse_code = open("input.txt", "r").read().split(" ")

morse_key = { 
".-"	:	"A",
"-..."	:	"B",
"-.-."	: 	"C",
"-.."	:	"D",
"."     :	"E",
"..-."	:	"F",
"--."	:	"G",
"...."	:	"H",
".."	:	"I",
".---"	:	"J",
"-.-"	:	"K",
".-.."	:	"L",
"--"	:	"M",
"-."	:	"N",
"---"	:	"O",
".--."	:	"P",
"--.-"	:	"Q",
".-."	:	"R",
"..."	:	"S", 		
"-"		:	"T",
"..-"	:	"U",
"...-"	:	"V",
".--"	:	"W",
"-..-"	:	"X",
"-.--"	:	"Y",
"--.."	:	"Z",
"-----"	:	"0",
".----"	:	"1",
"..---"	:	"2",
"...--"	:	"3",
"....-"	:	"4",
"....."	:	"5",
"-...."	:	"6",
"--..."	:	"7",
"---.."	:	"8",
"----."	:	"9",
"--..--" :	", ",
".-.-.-" :	".",
"..--.." :	"?",
"-..-."	 :	"/",
"-....-" :	"-",
"-.--."	 :	"(",
"-.--.-":	")",		 
}

plaintext = ""

for ch in morse_code:
    if ch == '{' or ch == '}':
        plaintext += ch
    else:
        plaintext += morse_key[ch]

print(plaintext)
