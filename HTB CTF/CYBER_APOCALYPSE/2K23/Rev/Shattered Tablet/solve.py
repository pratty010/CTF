"""
This is the Write Up for Reverse Engineering Challenge of Cyber Apocalypse 2K23 CTF - Shattered Tablet.

> Pratyush Prakhar (5#1NC#4N) - 03/20/20223

Description:
The challenge is about reverse engineering the binary `tablet.
We are greeted with a prompt on invoking the binary that gives us no information. Also, the common analysis techniques fail.

Solution:

1. Decode the binary to obtain the `main.c` file containing the main function for binary.
2. Contains lots of local variable that can be pieced together.
3. This script does just that to get the flag.
"""

#!/usr/bin/env python3

data = {
    'local_28._2_1_': 4,
    'local_38._4_1_': 3,
    'local_28._4_1_': 'r',
    'local_48._1_1_': 'T',
    'local_38._5_1_': 'v',
    'local_48._6_1_': 0,
    'local_28._7_1_': '}',
    'local_28._6_1_': 'd',
    'local_30._7_1_': 'r',
    'local_30._5_1_': 3,
    'local_40': 3,
    'local_38._6_1_': 'e',
    'local_28._3_1_': 1,
    'local_48._5_1_': 'r',
    'local_48': 'H',
    'local_28': 3,
    'local_38._2_1_': '.',
    'local_40._5_1_': 4,
    'local_48._3_1_': '{',
    'local_40._2_1_': '_',
    'local_38': '.',
    'local_48._4_1_': 'b',
    'local_48._7_1_': 'k',
    'local_40._7_1_': 't',
    'local_40._6_1_': 'r',
    'local_38._3_1_': 'n',
    'local_30._1_1_': 't',
    'local_38._1_1_': '.',
    'local_40._1_1_': 'n',
    'local_30._6_1_': '_',
    'local_30._2_1_': 0,
    'local_30': '_',
    'local_40._4_1_': 'p',
    'local_38._7_1_': 'r',
    'local_30._4_1_': 'b',
    'local_28._1_1_': 'p',
    'local_48._2_1_': 'B',
    'local_30._3_1_': '_',
    'local_40._3_1_': 4,
    'local_28._5_1_': 3
}


sorted_data = dict(sorted(data.items()))

output = {
    "local_28": "",
    "local_30": "",
    "local_38": "",
    "local_40": "",
    "local_48": ""
}
for key, value in sorted_data.items():
    v = key.split(".")[0]
    output[v] += str(value)

flag = "".join(values for key, values in (sorted(output.items(), reverse=True)))

print(flag)