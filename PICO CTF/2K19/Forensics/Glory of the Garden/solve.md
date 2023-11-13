# This Write Up is for the PICO CTF 2019 Forensics challenge - Glory of the Garden

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

This [garden](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Forensics/Glory%20of%20the%20Garden/garden.jpg) contains more than it seems.


## Solution

Simple `strings` operation to `grep` the flag.

```bash
└─$ strings garden.jpg | grep pico           
Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"
```

## FLAG

picoCTF{more_than_m33ts_the_3y3657BaB2C}