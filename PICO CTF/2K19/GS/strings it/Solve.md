# Write Up for General Skills challenge for PICO CTF 2K19 - strings it 

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Can you find the flag in [file](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/GS/strings%20it/strings) without running it?


## Solution

As the challenge suggests, we just need to `string` the program to get printable strings out of and `grep` for the flag.

```bash
└─$ strings strings | grep pico           
picoCTF{****************}
```

## FLAG

picoCTF{5tRIng5_1T_827aee91}
