# Write Up for General Skills challenge for PICO CTF 2K19 - plumbing

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag?\
Connect to jupiter.challenges.picoctf.org 7480.


## Solution

As the hint suggests, we can't read the mammoth amount of data coming in through the nc listener. WE can instead download it to a [file](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/GS/plumbing/out.txt) and then `grep` for the flag.

```bash
└─$ nc jupiter.challenges.picoctf.org 7480 > out.txt 
                                                                                                                                  
└─$ cat out.txt| grep pico
picoCTF{****************************}
```

## FLAG

picoCTF{digital_plumb3r_06e9d954}







