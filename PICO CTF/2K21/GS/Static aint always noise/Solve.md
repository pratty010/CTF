# Write Up for General Skills challenge for PICO CTF 2K21 - Static ain't always noise.

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Can you look at the data in this [binary](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K21/GS/Static%20aint%20always%20noise/static): static? This [BASH script](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K21/GS/Static%20aint%20always%20noise/ltdis.sh) might help!

## Solution

1. We get a static file which we can look around and get the flag directly.
2. What the bash script is doing, is [disassembling the binary](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K21/GS/Static%20aint%20always%20noise/static.ltdis.x86_64.txt) with `objdump` and extracting [useful strings](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K21/GS/Static%20aint%20always%20noise/static.ltdis.strings.txt) from offset using `strings`.
3. We can get the flag from the second file too.

```bash
└─$ ./ltdis.sh 
Attempting disassembly of  ...
objdump: 'a.out': No such file
objdump: section '.text' mentioned in a -j option, but not found in any input file
Disassembly failed!
Usage: ltdis.sh <program-file>
Bye!
                                                                                                                                  
└─$ ./ltdis.sh static 
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset

└─$ cat static.ltdis.strings.txt| grep pico
   1020 picoCTF{***********************}

```

## FLAG

picoCTF{d15a5m_t34s3r_f6c48608}







