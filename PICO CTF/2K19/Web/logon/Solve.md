# Write Up for Web Exploit challenge for PICO CTF 2K19 - logon 

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

The factory is hiding things from all of its users.\
Can you login as Joe and find what they've been looking at?\ 
https://jupiter.challenges.picoctf.org/problem/13594/ (link) or http://jupiter.challenges.picoctf.org:13594

[WebSite Main Page](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/logon/images/web.png)

## Solution

1. We land up on a login page.

2. When we try to login as `joe` with no password, we get a message that we can't access the flag.
![](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/logon/images/login.png)

3. we can now explore the cookies. We see the **admin** cookie is set to **False**. What if we turn it to **True** and reload. We get the flag.
![](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/logon/images/flag.png)

## FLAG

picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}