# Write Up for Web Exploit challenge for PICO CTF 2K23 - chrono

> Pratyush Prakhar (5#1NC#4N) - 11/11/2023

## Description

How to automate tasks to run at intervals on linux servers?

## Solution

The challenge hints towards `cron jobs` which is a way to schedule actions or jobs to run/execute automatically on Linux Severs at set frequencies. Let's look into the `/etc/crontab` file that contains all this information.

```bash
picoplayer@challenge:~$ cd /etc/
Display all 109 possibilities? (y or n)
picoplayer@challenge:~$ cat /etc/crontab
# picoCTF{*****************************}
```

## FLAG

picoCTF{Sch3DUL7NG_T45K3_L1NUX_9d5cb744}
