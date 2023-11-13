# Write Up for General Skills challenge for PICO CTF 2K19 - Based

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary.\
Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc jupiter.challenges.picoctf.org 29221.

## Solution

The challenge comes with a questionnaire through anc listener. This asks us to convert inputs from multiple formats to ASCII. We can use [CyberChef](https://cyberchef.org/) to solve each puzzle within the timeout.

```bash
└─$ nc jupiter.challenges.picoctf.org 29221
Let us see how data is stored
lamp
Please give the 01101100 01100001 01101101 01110000 as a word.
...
you have 45 seconds.....

Input:
lamp
Please give me the  146 141 154 143 157 156 as a word.
Input:
falcon
Please give me the 70656172 as a word.
Input:
pear
You've beaten the challenge
Flag: picoCTF{*******************************************}
```

## FLAG

picoCTF{learning_about_converting_values_00a975ff}







