# This is the Write Up for day 2 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/03/2019

## Description

A big part of working at the best festival company is the social live! The elves have always loved interacting with everyone. Unfortunately, the christmas monster took down their main form of communication - the arctic forum! 

Elf McForum has been sobbing away McElferson's office. How could the monster take down the forum! In an attempt to make McElferson happy, she sends you to McForum's office to help. 

`This challenge is all about protecting your passwords properly or as hackers call it A07:2021-Identification and Authentication Failures.`

## Solution

1. We again land on a login page for something called `arctic forum.` Let's try some basic sql injection for fun. But we don't get any luck through this.
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_2/images/login.png)

2. So, let's continue our hunt for the hidden page as mentioned in the challenge. We run a simple `feroxbuster scan`. The [results](ferox.txt) points us towards the `/sysadmin` page. But now what about the cred's again. The task hint's towards `default creds`. So, rather than brute force, let's OSINT.
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_2/images/admin.png)

3. On exploring the www, we find the following [github repo](https://github.com/ashu-savani/arctic-digital-design) for the arctic forum created just today. Strange!! Someone is helping us or everyone. But let's try to use the credentials presented here.

4. We get in using these creds. I had little hopes for that but lesson learned. Don't leave credentials of your admin portal on the WWW. 
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_2/images/portal.png)

5. It has one entry for us. Let's look into that and end our day.


## Brownie Points

1. What is the path of the hidden page? - **/sysadmin** 

2 What is the password you found? - **admin:defaultpass**

3. What do you have to take to the 'partay'? - **Eggnog**

## Extra Treats

1. Additional ports open on the same IP - [rustscan file](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_2/all.nmap)
