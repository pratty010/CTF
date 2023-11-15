# This is the Write Up for day 3 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/04/2019

## Description

An Elf-ministrator, has a [network capture file](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_3/Evil%20Elf.pcap) from a computer and needs help to figure out what went on! Are you able to help?

`This challenge is all about logging incidents properly or it can result into what hackers call it A09:2021-Security Logging and Monitoring Failures.`

## Solution

Using our old friend `wireshark` for exploring. This is not a tutorial. But will drop some hints.

## Brownie Points

1. Whats the destination IP on packet number 998? - **63.32.89.195** --> The packets are numbered properly.
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_3/images/packet.png)

2. What item is on the Christmas list? - **ps4** --> Follow TCP streams.

3. Crack buddy's password! - **rainbow** --> Use hashcat on the data collected.

