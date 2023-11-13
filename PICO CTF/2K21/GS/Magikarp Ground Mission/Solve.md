# Write Up for General Skills challenge for PICO CTF 2K21 - Magikarp Ground Mission.

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Do you know how to move between directories and read files in the shell?\
Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `b60940ca`

## Solution

Simple dir traversal challenge. Follow Along.


```bash
└─$     ssh ctf-player@venus.picoctf.net -p 53689
The authenticity of host '[venus.picoctf.net]:53689 ([3.131.124.143]:53689)' can't be established.
ED25519 key fingerprint is SHA256:P1f6h95BrSVnJbm2AKhphfHHGEyAeThib/rN/AwKs24.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[venus.picoctf.net]:53689' (ED25519) to the list of known hosts.
ctf-player@venus.picoctf.net's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat 1of3.flag.txt 
picoCTF{xxsh_
ctf-player@pico-chall$ cat instructions-to-2of3.txt 
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls -la
total 92
drwxr-xr-x   1 root root 4096 Nov 13 08:08 .
drwxr-xr-x   1 root root 4096 Nov 13 08:08 ..
-rwxr-xr-x   1 root root    0 Nov 13 08:08 .dockerenv
-rw-r--r--   1 root root   17 Mar 16  2021 2of3.flag.txt
drwxr-xr-x   1 root root 4096 Mar 16  2021 bin
drwxr-xr-x   2 root root 4096 Apr 24  2018 boot
drwxr-xr-x   5 root root  340 Nov 13 08:08 dev
drwxr-xr-x   1 root root 4096 Nov 13 08:08 etc
drwxr-xr-x   1 root root 4096 Mar 16  2021 home
-rw-r--r--   1 root root   51 Mar 16  2021 instructions-to-3of3.txt
drwxr-xr-x   1 root root 4096 Mar 16  2021 lib
drwxr-xr-x   2 root root 4096 Feb 22  2021 lib64
drwxr-xr-x   2 root root 4096 Feb 22  2021 media
drwxr-xr-x   2 root root 4096 Feb 22  2021 mnt
drwxr-xr-x   1 root root 4096 Mar 16  2021 opt
dr-xr-xr-x 190 root root    0 Nov 13 08:08 proc
drwx------   2 root root 4096 Feb 22  2021 root
drwxr-xr-x   1 root root 4096 Nov 13 08:09 run
drwxr-xr-x   1 root root 4096 Mar 16  2021 sbin
drwxr-xr-x   2 root root 4096 Feb 22  2021 srv
dr-xr-xr-x  13 root root    0 Nov 13 08:08 sys
drwxrwxrwt   1 root root 4096 Mar 16  2021 tmp
drwxr-xr-x   1 root root 4096 Feb 22  2021 usr
drwxr-xr-x   1 root root 4096 Feb 22  2021 var
ctf-player@pico-chall$ cat 2of3.flag.txt 
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$ cat instructions-to-3of3.txt 
Lastly, ctf-player, go home... more succinctly `~`
ctf-player@pico-chall$ cd ~
ctf-player@pico-chall$ ls -la
total 32
drwxr-xr-x 1 ctf-player ctf-player 4096 Nov 13 08:09 .
drwxr-xr-x 1 root       root       4096 Mar 16  2021 ..
drwx------ 2 ctf-player ctf-player 4096 Nov 13 08:09 .cache
-rw-r--r-- 1 ctf-player ctf-player   80 Mar 16  2021 .profile
drw------- 1 ctf-player ctf-player 4096 Mar 16  2021 .ssh
-rw-r--r-- 1 ctf-player ctf-player   10 Mar 16  2021 3of3.flag.txt
drwxr-xr-x 1 ctf-player ctf-player 4096 Mar 16  2021 drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt 
c1754242}
ctf-player@pico-chall$
```


## FLAG

picoCTF{xxsh_0ut_0f_\/\/4t3r_c1754242}