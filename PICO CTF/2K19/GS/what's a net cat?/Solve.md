# Write Up for General Skills challenge for PICO CTF 2K19 - what's a net cat

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Using netcat (nc) is going to be pretty important.\
Can you connect to jupiter.challenges.picoctf.org at port 64287 to get the flag?

## Solution

As the challenge suggests, we just need to `nc` at given address and port to receive data flushed to the listener.

```bash
└─$ nc  jupiter.challenges.picoctf.org 64287          
You're on your way to becoming the net cat master
picoCTF{*************************}
```

## FLAG

picoCTF{nEtCat_Mast3ry_284be8f7}
