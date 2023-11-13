# This Write Up is for the PICO CTF 2019 Forensics challenge - So Meta

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Find the flag in this [picture](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Forensics/So%20Meta/pico_img.png).

## Solution

Simple `exiftool` to read the metadata of the image


```bash
└─$ exiftool pico_img.png               
ExifTool Version Number         : 12.67
File Name                       : pico_img.png
Directory                       : .
File Size                       : 109 kB
File Modification Date/Time     : 2020:10:27 00:08:23+05:30
..................................................................
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{****************}
Image Size                      : 600x600
Megapixels                      : 0.360
```

## FLAG

picoCTF{s0_m3ta_fec06741}
