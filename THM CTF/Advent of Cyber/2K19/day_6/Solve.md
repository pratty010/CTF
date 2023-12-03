# This is the Write Up for day 6 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/06/2019

## Description

"McElferson! McElferson! Come quickly!" yelled Elf-ministrator.

"What is it Elf-ministrator?" McElferson replies.

"Data has been stolen off of our servers!" Elf-ministrator says!

"What was stolen?" She replied.

"I... I'm not sure... They hid it very well, all I know is something is missing" they replied.

"I know just who to call" said McElferson...

`This challenge is all about packet analysis`

## Solution

1. We get a pcap capture file that can be analyzed with `wireshark`.

2. Let's first look into the `DNS protocol`. There is a domain that is being ex-filtrated through DNS - `43616e64792043616e652053657269616c204e756d6265722038343931.holidaythief.com`. This seems to be obfuscated on purpose. Let's decode the first part using our friend [CyberChef](https://cyberchef.org/#recipe=From_Hex('None')&input=NDM2MTZlNjQ3OTIwNDM2MTZlNjUyMDUzNjU3MjY5NjE2YzIwNGU3NTZkNjI2NTcyMjAzODM0MzkzMQ). We get the data as _Candy Cane Serial Number 8491_.

3. Now let's explore the HTTP streams. We, find that there are 2 artifacts that are downloaded - [christmaslists.zip](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_6/christmaslists/christmaslists.zip) and [TryHackMe.jpg](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_6/TryHackMe.jpg). Let's export these HTTP objects and examine them.

4. On exploring the christmas lists, we find the zip is password protected and needs to be cracked. Let's rely on our old friend John for this. We can now unzip using the [cracked password](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_6/christmaslists/passwd) to obtain multiple christmas lists.

```bash
└─$ zip2john christmaslists.zip > hash    
ver 1.0 efh 5455 efh 7875 christmaslists.zip/christmaslistdan.tx PKZIP Encr: 2b chk, TS_chk, cmplen=91, decmplen=79, crc=FF67349B ts=9A34 cs=9a34 type=0
ver 2.0 efh 5455 efh 7875 christmaslists.zip/christmaslistdark.txt PKZIP Encr: TS_chk, cmplen=91, decmplen=82, crc=5A38B7BB ts=9A4D cs=9a4d type=8
ver 2.0 efh 5455 efh 7875 christmaslists.zip/christmaslistskidyandashu.txt PKZIP Encr: TS_chk, cmplen=108, decmplen=116, crc=BCA00B27 ts=9A74 cs=9a74 type=8
ver 2.0 efh 5455 efh 7875 christmaslists.zip/christmaslisttimmy.txt PKZIP Encr: TS_chk, cmplen=105, decmplen=101, crc=7069EA51 ts=9A11 cs=9a11 type=8
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
                                                                                                                                  
└─$ john hash --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
```

5. We can now get what each child wants for christmas.

```bash
└─$ unzip christmaslists.zip 
Archive:  christmaslists.zip
[christmaslists.zip] christmaslistdan.tx password: 
 extracting: christmaslistdan.tx     
  inflating: christmaslistdark.txt   
  inflating: christmaslistskidyandashu.txt  
  inflating: christmaslisttimmy.txt  
                                                                                                                                  
└─$ ls -la
total 36
drwxr-xr-x 2 kali kali 4096 Nov 14 01:26 .
drwxr-xr-x 3 kali kali 4096 Nov 14 01:21 ..
-rw-r--r-- 1 kali kali   79 Dec  4  2019 christmaslistdan.tx
-rw-r--r-- 1 kali kali   82 Dec  4  2019 christmaslistdark.txt
-rw-r--r-- 1 kali kali  116 Dec  4  2019 christmaslistskidyandashu.txt
-rw-r--r-- 1 kali kali 1175 Nov 14 01:20 christmaslists.zip
-rw-r--r-- 1 kali kali  101 Dec  4  2019 christmaslisttimmy.txt
-rw-r--r-- 1 kali kali  654 Nov 14 01:23 hash
-rw-r--r-- 1 kali kali  198 Nov 14 01:24 passwd
                                                                                                                                  
└─$ cat christmaslisttimmy.txt
Dear Santa,
For Christmas I would like to be a PenTester! Not the Bic kind!
Thank you,
Little Timmy.
```

6. Let's now explore the other image we obtained for similar hidden information. We can use a stenography wiz - `steghide` expert in this kind of work. To our surprise, the creator left the door open with no passphrase required. Let's nwo extract the embedded data.

```bash
└─$ steghide --info TryHackMe.jpg 
"TryHackMe.jpg":
  format: jpeg
  capacity: 1.4 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "christmasmonster.txt":
    size: 1.7 KB
    encrypted: rijndael-128, cbc
    compressed: yes
                                                                                                                                  
└─$ steghide extract -sf TryHackMe.jpg
Enter passphrase: 
wrote extracted data to "christmasmonster.txt".
```

7. We can then view this embedded [file](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_6/christmasmonster.txt) to get the hidden data. Information about `RFC527 - ARPAWOCKY`.


## Brownie Points

1. What data was exfiltrated via DNS? - **Candy Cane Serial Number 8491**.

2. What did Little Timmy want to be for Christmas? - **PenTester**.

3. What was hidden within the file? - **RFC527**.


## Extra Treats

1. We get christmas lists of [all](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_6/christmaslists). Some of them are quite interesting.

2. What is this [RFC](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_6/christmasmonster.txt)?