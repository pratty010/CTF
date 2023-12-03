"""
This is the Write Up for day 9 challenge of Advent of Cyber 2K19 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/09/2019

Description:
McSkidy has been going keeping inventory of all the infrastructure but he finds a random web server running on port 3000. All he receives when accessing '/' is {"value":"s","next":"f"}

McSkidy needs to access the next page at /f(which is the value received from the data above) and keep track of the value at each step(in this case 's'). McSkidy needs to do this until the 'value' and 'next' data have the value equal to 'end'.

You can access the machines at the following IP:
10.10.169.100


Solution:

Simple linear requests to the next param and record the value param as flag.
"""

#!/usr/bin/env python3

import requests, json

URL = "http://10.10.169.100:3000/"

res = requests.get(URL)
data = json.loads(res.text)

flag = data["value"]

while data["next"] != "end":

    print("Current flag value - {}".format(flag))

    n = data["next"]
    print("Next value found as {}. Trying URL {}".format(n, URL+n))

    res = requests.get(URL+n)
    data = json.loads(res.text)

    if data["value"] != "end":
        flag += data["value"]

    
print("Final flag value - {}".format(flag))