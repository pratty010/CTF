# Write Up for Web Exploit challenge for PICO CTF 2K19 - picobrowser

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

This website can be rendered only by picobrowser, go and catch the flag!\
https://jupiter.challenges.picoctf.org/problem/26704/ (link) or http://jupiter.challenges.picoctf.org:26704

[WebSite Main Page](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/picobrowser/images/web.png)

## Solution

1. We land up on a `default click me flag page` again. 

2. On clicking the flag option, we get *not picobrowser but out user agent*. This means that we might have to change the `User-Agent` to get access to the flag.
![](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/picobrowser/images/issue.png)
\
\
![](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/picobrowser/images/user_agent.png)

3. We can get the flag after changing the `User-Agent` to `picobrowser`.
![](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K19/Web/picobrowser/images/flag.png)



## FLAG

picoCTF{p1c0_s3cr3t_ag3nt_e9b160d0}
