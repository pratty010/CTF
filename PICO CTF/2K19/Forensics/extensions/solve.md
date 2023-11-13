# This Write Up is for the PICO CTF 2019 Forensics challenge - extensions.

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

This is a really weird text file [TXT](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Forensics/extensions/flag.png)? Can you find the flag?

## Solution

1. On reading the file, we find that it is not a `text` file but is saved as one. Can be confirmed here using `file` command.

```bash
└─$ file flag.txt    
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```

2. To our surprise it is a `.png` file. So let's save it as one and view it. Oh, Oh, here is the flag.

```bash
└─$ cp flag.txt flag.png 
```

## FLAG

picoCTF{now_you_know_about_extensions}
