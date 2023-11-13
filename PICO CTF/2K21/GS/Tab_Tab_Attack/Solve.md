# Write Up for General Skills challenge for PICO CTF 2K21 - Tab,TAb,Attack.

> Pratyush Prakhar (5#1NC#4N) - 08/09/2023

## Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://github.com/pratty010/CTF/blob/master/PICO%20CTF/2K21/GS/Tab_Tab_Attack/Addadshashanammu.zip)

## Solution

Simple tab autocomplete to reach to the binary file and execute it.

```bash
└─$ tree .
.
├── Addadshashanammu
│   └── Almurbalarammi
│       └── Ashalmimilkala
│           └── Assurnabitashpi
│               └── Maelkashishi
│                   └── Onnissiralis
│                       └── Ularradallaku
│                           └── fang-of-haynekhtnamet
└── Addadshashanammu.zip

8 directories, 2 files
                                                                                                                                  
└─$ ./Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet                  
*ZAP!* picoCTF{***********************************}
```

## FLAG

picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}