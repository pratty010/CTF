# This is the Write Up for Web challenge of Cyber Apocalypse 2K23 CTF - Trapped Source

> Pratyush Prakhar (5#1NC#4N) - 03/20/2022

## Description

1. Web Challenge running on 209.97.140.29:31962. Greeted with a `4 digit pin` lock.

2. Need to supply the right pin to get in. Can brute force it but let's first see for any low hanging fruit.

## Solution

1. Checking the `page source` on the sit to get the correct pin --> `1356`.

!()[https://github.com/pratty010/CTF/blob/master/HTB%20CTF/CYBER_APOCALYPSE/2K23/Web/Trapped%20Source/images/ps.png]

2. Obtain flag on the login with correct pin.

!()[https://github.com/pratty010/CTF/blob/master/HTB%20CTF/CYBER_APOCALYPSE/2K23/Web/Trapped%20Source/images/flag.png]
