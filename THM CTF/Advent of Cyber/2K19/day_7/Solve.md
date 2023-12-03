# This is the Write Up for day 7 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/07/2019

## Description

Previously, we saw mcsysadmin learning the basics of Linux. With the on-going crisis, McElferson has been very impressed and is looking to push mcsysadmin to the security team. One of the first things they have to do is look at some strange machines that they found on their network. 

`This challenge is all about port scanning.`

## Solution

1. We find all the ports open with our nmap on steriods - `rustscan`. The scan file can be found [here](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_7/rustscan/all.nmap).

2. We can then run a full blown scripts scan against the found ports. Results stored [here](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_7/rustscan/main.nmap).

3. we find that a web server is active at `port 999`. On exploring it has a [file](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_7/interesting.file) listed out.
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_7/web.png).

4. Feel free to poke around other ports and hosted services. The End.


## Brownie Points

1. how many TCP ports under 1000 are open? - **3**.

2. What is the name of the OS of the host? - **Linux**.

3. What version of SSH is running? - **7.4**.

4. What is the name of the file that is accessible on the server you found running? - **interesting.file**



