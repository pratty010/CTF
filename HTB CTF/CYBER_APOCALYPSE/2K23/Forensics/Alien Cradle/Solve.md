# This is the Write Up for Forensics challenge of Cyber Apocalypse 2K23 CTF - Alien Cradle.

> Pratyush Prakhar (5#1NC#4N) - 03/20/2022

## Description

Given a `powershell file` [here](https://github.com/pratty010/CTF/blob/master/HTB%20CTF/CYBER_APOCALYPSE/2K23/Forensics/Alien%20Cradle/cradle.ps1)

Need to get the flag hidden in it.

## Solution

1. Examining the `cradle.ps1` file we find the following:
```powershell
$f = 'H' + 'T' + 'B' + '{p0w3rs' + 'h3ll' + '_Cr4d' + 'l3s_c4n_g3t' + '_th' + '3_j0b_d' + '0n3}'
```
2. We can see that the flag is split into multiple parts and concatenated together. We can use the following command in powershell to get the flag:

```powershell
> echo $f
HTB{p0w3rsh3ll_Cr4dl3s_c4n_g3t_th3_j0b_d0n3}
```
