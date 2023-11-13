# Write Up for General Skills challenge for PICO CTF 2K19 - Bases

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

## Solution

As the challenge suggests, the given string might be encoded with a certain `base*` format. We find it to be `Base64`. We get the flag by easily decoding it.

```bash
└─$ echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
*****************************
```

## FLAG

picoCTF{l3arn_th3_r0p35}







