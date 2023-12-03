# This is the Write Up for day 5 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/05/2019

## Description

Elf Lola is an elf-of-interest. Has she been helping the Christmas Monster? lets use all available data to find more information about her! We must protect The Best Festival Company!

`This challenge is all about OSINT.`

## Solution

1. We get a picture of a grinch from the recovery. Let's explore it with `exiftool`, `strings` and `steghide` for metadata.

```bash
└─$ exiftool thegrinch.jpg 
ExifTool Version Number         : 12.67
File Name                       : thegrinch.jpg
Directory                       : .
File Size                       : 71 kB
File Modification Date/Time     : 2023:11:13 20:19:00+05:30
File Access Date/Time           : 2023:11:13 20:20:32+05:30
File Inode Change Date/Time     : 2023:11:13 20:19:38+05:30
File Permissions                : -rwxrw-rw-
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
XMP Toolkit                     : Image::ExifTool 10.10
Creator                         : JLolax1
Image Width                     : 642
Image Height                    : 429
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 642x429
Megapixels                      : 0.275
```

2. We see that the Creator has an alias of `JLolax1`. we can search around for this alias on internet to maybe get some information on her. (Hint from the task.)

3. To our surprise (not really!), she has a [twitter account](https://twitter.com/jlolax1). This provides us required useful information such DOB, occupation, relevant tweets. 

4. She also has a [wordpress website](https://lolajohnson1998.wordpress.com/) for her photography portfolio. We can use the information from these photos to get the rest of the answer. But we don't for when the first picture was clicked. 

5. Let's look into an amazing tool, when we want to look into the history of a website - [Wayback Machine](http://web.archive.org/). The [first snapshot](http://web.archive.org/web/20191023204639/https://lolajohnson1998.wordpress.com/) of the website shows that it looked different when created then.
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_5/wordpress/first.png)

6. The text reads, it was created 5 years ago from the date of snapshot. The day is now complete with this research.

## Brownie Points

1. What is Lola's date of birth? Format: Month Date, Year(e.g November 12, 2019) - **December 29, 1900**.

2. What is Lola's current occupation? - **Santa's Helper**.

3. What phone does Lola make? - **iPhone X**.

4. What date did Lola first start her photography? Format: dd/mm/yyyy - **23/10/2014**

5. What famous woman does Lola have on her web page? - **Ada Lovelace**.

