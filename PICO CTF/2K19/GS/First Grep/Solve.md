# Write Up for General Skills challenge for PICO CTF 2K19 - First Grep

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Can you find the flag in [file](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/GS/First%20Grep/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Solution

As the challenge suggests, we will have to `grep` for the flag out of the file for a quick win.

```bash
└─$ cat file | grep pico
picoCTF{***************************}
```

## FLAG

picoCTF{grep_is_good_to_find_things_dba08a45}







