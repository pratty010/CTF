# This is the Write Up for day 4 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/05/2019

## Description

With the entire incident, McElferson has been very stressed.

We need all hands on deck now

To help resolve things faster, she has asked you to help the new intern(mcsysadmin) get familiar with Linux.

SSH details:
username: mcsysadmin
password: bestelf1234

`This challenge is all about Linux/System Enumeration.`

## Solution

SSH into the system with the creds and look into each tasks.

## Brownie Points

1. How many visible files are there in the home directory(excluding ./ and ../)? - **8**

```bash
[mcsysadmin@ip-10-10-228-248 ~]$ ls -la
total 136
drwx------ 2 mcsysadmin mcsysadmin   199 Dec  4  2019 .
drwxr-xr-x 4 root       root          40 Dec  4  2019 ..
-rw------- 1 mcsysadmin mcsysadmin   119 Dec  4  2019 .bash_history
-rw-r--r-- 1 mcsysadmin mcsysadmin    18 Jul 27  2018 .bash_logout
-rw-r--r-- 1 mcsysadmin mcsysadmin   193 Jul 27  2018 .bash_profile
-rw-r--r-- 1 mcsysadmin mcsysadmin   231 Jul 27  2018 .bashrc
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file1
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file2
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file3
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file4
-rw-rw-r-- 1 mcsysadmin mcsysadmin     8 Dec  4  2019 file5
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file6
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file7
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file8
-rw------- 1 mcsysadmin mcsysadmin  1024 Dec  4  2019 .rnd
```

2. What is the content of file5? - **recipes**

```bash
[mcsysadmin@ip-10-10-228-248 ~]$ cat file5
recipes
```

3. Which file contains the string ‘password’? - **file6**

```bash
[mcsysadmin@ip-10-10-228-248 ~]$ grep "password" file*
file6:passwordHpKRQfdxzZocwg5O0RsiyLSVQon72CjFmsV4ZLGjxI8tXYo1NhLsEply
[mcsysadmin@ip-10-10-228-248 ~]$ for file in file*; do echo "$file"; cat "$file" | grep "password" ;done
file1
file2
file3
file4
file5
file6
passwordHpKRQfdxzZocwg5O0RsiyLSVQon72CjFmsV4ZLGjxI8tXYo1NhLsEply
file7
file8
```

4. What is the IP address in a file in the home folder? - **10.0.0.05**

```bash
# Regex check for only matching pattern of IPv4
[mcsysadmin@ip-10-10-228-248 ~]$ grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" file*
file2:10.0.0.05
```

5. How many users can log into the machine? - **3**

```bash
[mcsysadmin@ip-10-10-228-248 ~]$ cat /etc/passwd | grep sh$
root:x:0:0:root:/root:/bin/bash
ec2-user:x:1000:1000:EC2 Default User:/home/ec2-user:/bin/bash
mcsysadmin:x:1001:1001::/home/mcsysadmin:/bin/bash
```

6. What is the sha1 hash of file8? - **fa67ee594358d83becdd2cb6c466b25320fd2835**

```bash
[mcsysadmin@ip-10-10-228-248 ~]$ sha1sum file8
fa67ee594358d83becdd2cb6c466b25320fd2835  file8
```

7. What is mcsysadmin’s password hash? - **$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/**

```bash
[mcsysadmin@ip-10-10-228-248 ~]$ find / -name "*shadow*" 2>/dev/null 
/etc/gshadow
/etc/shadow
/etc/shadow-
/etc/gshadow-
/var/shadow.bak
/usr/lib64/libuser/libuser_shadow.so
.............................................................................
[mcsysadmin@ip-10-10-228-248 ~]$ ls -al /var/shadow.bak
-rwxr-xr-x 1 root root 783 Dec  4  2019 /var/shadow.bak
[mcsysadmin@ip-10-10-228-248 ~]$ cat /var/shadow.bak
root:*LOCK*:14600::::::
bin:*:17919:0:99999:7:::
daemon:*:17919:0:99999:7:::
adm:*:17919:0:99999:7:::
lp:*:17919:0:99999:7:::
sync:*:17919:0:99999:7:::
shutdown:*:17919:0:99999:7:::
halt:*:17919:0:99999:7:::
mail:*:17919:0:99999:7:::
operator:*:17919:0:99999:7:::
games:*:17919:0:99999:7:::
ftp:*:17919:0:99999:7:::
nobody:*:17919:0:99999:7:::
systemd-network:!!:18218::::::
dbus:!!:18218::::::
rpc:!!:18218:0:99999:7:::
libstoragemgmt:!!:18218::::::
sshd:!!:18218::::::
rpcuser:!!:18218::::::
nfsnobody:!!:18218::::::
ec2-instance-connect:!!:18218::::::
postfix:!!:18218::::::
chrony:!!:18218::::::
tcpdump:!!:18218::::::
ec2-user:!!:18234:0:99999:7:::
mcsysadmin:$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/:18234:0:99999:7:::
```
