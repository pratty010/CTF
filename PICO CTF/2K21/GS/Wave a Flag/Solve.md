# Write Up for General Skills challenge for PICO CTF 2K21 - Wave a flag.

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Can you invoke help flags for a tool or binary?\
This [program](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K21/GS/Wave%20a%20Flag/warm) has extraordinarily helpful information...

## Solution

Multiple ways to solve this. Some shown below.

```bash
└─$ ./warm              
Hello user! Pass me a -h to learn what I can do!
└─$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{*******************************}
└─$ strings warm | grep pico
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{*******************************}
```

## FLAG

picoCTF{b1scu1ts_4nd_gr4vy_30e77291}







