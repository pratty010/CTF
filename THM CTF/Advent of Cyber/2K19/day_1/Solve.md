# This is the Write Up for day 1 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/01/2019

## Description

Elves needed a way to submit their inventory - have a web page where they submit their requests and the elf mcinventory can look at what others have submitted to approve their requests. It’s a busy time for mcinventory as elves are starting to put in their orders. mcinventory rushes into McElferson’s office.

I don’t know what to do. We need to get inventory going. Elves can log on but I can’t actually authorise people’s requests! How will the rest start manufacturing what they want.  

McElferson calls you to take a look at the website to see if there’s anything you can do to help. Deploy the machine and access the website at http://<your_machines_ip>:3000 - it can take up to 3 minutes for your machine to boot!

`This challenge is all about protecting your cookies properly or as hackers call it A04:2021-Insecure Design.`

## Solution

1. On going to the said webpage, we are greeted with a login form. We can't login with out proper set of credentials.
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_1/images/login.png)

2. So, rather than brute-forcing the form or before we fall for that path, let's look at the register page to gather more information about maybe `cookies` and `back-end`. Let's run it through a proxy so, we can get the `request-response` model.
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_1/images/register.png)

3. On doing that and logging in as our user `shinchan`, we get to the `/home` page which allows us to add some items to the `inventory`. But how is it keeping track of the _session_? There must be some **cookie** to eat. Let's munch on it.
![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_1/images/home.png)

4. We find that there is an auth cookie in play with the name as `authid` and it is storing some value which looks like a `Base*` value. That is some weak s**t. Let's play with it. What do we have here?

```bash
└─$ echo c2hpbmNoYW52NGVyOWxsMSFzcw== | base64 -d
shinchanv4er9ll1!ss
```

5. We suspect that there is something strange happening, so let's confirm it. This is not how any cookies are stored.
    1. create another user - `himwari`.
    2. get the cookie stored for her in the same way.
    ![](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_1/images/cookie_check.png)
    3. Decode the cookie in the same way.
    ```bash
    └─$ echo aGltYXdhcml2NGVyOWxsMSFzcw== | base64 -d
    himawariv4er9ll1!ss  
    ```
    4. Oh My Santa, what do we have here. It seems some bozo, is just creating cookies in this format `base64(<username>v4er9ll1!ss)`

6. Now let's become admin (mcinventory) by reverse engineering the cookie.
    1. admin cookie in plain text - _mcinventoryv4er9ll1!ss_.
    2. Based cookie - _bWNpbnZlbnRvcnl2NGVyOWxsMSFzcwo=_.
    ```bash
    └─$ echo 'mcinventoryv4er9ll1!ss'  | base64 
    bWNpbnZlbnRvcnl2NGVyOWxsMSFzcwo=
    ```
    3. Replace the `authid` with our new cookie for a session hijacking attack.
    4. And what do we see. The [inventory portal](https://github.com/pratty010/CTF/blob/master/THM%20CTF/Advent%20of%20Cyber/2K19/day_1/images/mcinventory.png) of mcinventory.

7. There is a huge security issue afoot as `firewall` request has been rejected.


## Brownie Points

1. What is the name of the cookie used for authentication? - **authid**.

2. If you decode the cookie, what is the value of the fixed part of the cookie? - **v4er9ll1!ss**.

3. After accessing his account, what did the user mcinventory request? - **firewall**.
