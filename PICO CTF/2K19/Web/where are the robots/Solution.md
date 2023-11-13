# Write Up for Web Exploit challenge for PICO CTF 2K19 - where are the robots

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Can you find the robots?\
https://jupiter.challenges.picoctf.org/problem/36474/ (link) or http://jupiter.challenges.picoctf.org:36474

[WebSite Main Page](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/where%20are%20the%20robots/images/web.png)

## Solution

1. The challenge is centered around exploring the `/robots.txt` [file](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/where%20are%20the%20robots/images/robots.png) which disallows the web listings to be disallowed from spidering.

2. It has an entry for `/477ce.html`. We can now manually go to this page.

3. On visiting this page, we obtain the [flag](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/where%20are%20the%20robots/images/flag.png).


## FLAG

picoCTF{ca1cu1at1ng_Mach1n3s_477ce}
