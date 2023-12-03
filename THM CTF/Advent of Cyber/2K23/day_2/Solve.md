# This is the Write Up for day 2 challenge of Advent of Cyber 2K23 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/02/2023

## Description

After yesterday’s resounding success, McHoneyBell walks into AntarctiCrafts’ office with a gleaming smile. She takes out her company-issued laptop from her knapsack and decides to check the news. “Traffic on the North-15 Highway? Glad I skied into work today,” she boasts. A notification from the Best Festival Company’s internal communication tool (HollyChat) pings.

It’s another task. It reads, “The B-Team has been tasked with understanding the network of AntarctiCrafts’ South Pole site”. Taking a minute to think about the task ahead, McHoneyBell realises that AntarctiCrafts has no fancy technology that captures events on the network. “No tech? No problem!” exclaims McHoneyBell.

She decides to open up her Python terminal…

`This challenge is all about Log Analysis through Python Pandas library`

## Solution

1. The supplies CSV file contains information about network packets, their source and destination, and protocol used. This can be a obtained from a general packet reader. But to make sense of all the data, we need to summarize that information to get fruitful results. Sample results are as follows

```py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('network_traffic.csv')
df.head(5)
```

**Results**
```bash
 	PacketNumber 	Timestamp 	Source 	   Destination 	Protocol
0 	    1 	         05:49.5   10.10.1.7 	10.10.1.9 	  HTTP
1 	    2 	         05:50.3   10.10.1.10 	10.10.1.3 	  TCP
2 	    3 	         06:10.3   10.10.1.1 	10.10.1.2 	  HTTP
3 	    4 	         06:10.4   10.10.1.9 	10.10.1.3 	  ICMP
4 	    5 	         06:10.4   10.10.1.1 	10.10.1.7 	  ICMP
```

2. If we want to know how many total packets were captured, we can simply get the total count of the `dataframe` which would be all the packets.

```py
# Question 2
# Here you will need to use Pandas count function on the dataframe
# We just count the count of the Packet Number Column.

df["PacketNumber"].count()
```

**Results**
```bash
100
```

3. To known what IP source sent the ost traffic, we just need to group the `Source` column based on their frequency. We can use `size` function for that. We can then sort them in descending order based on the values.

```py
#Question 3
# Here you can perform a groupby with Pandas size function on the Source and Destination columns

df.groupby(['Source']).size().sort_values(ascending=False)
```

**Results**
```bash
Source
10.10.1.4     15
10.10.1.6     14
10.10.1.3     13
10.10.1.2     12
10.10.1.9     11
10.10.1.8      9
10.10.1.1      8
10.10.1.10     8
10.10.1.5      5
10.10.1.7      5
dtype: int64
```

4. For the most used protocol, we can use the above logic but for `Protocol` column.

```py
#Question 4
# Here you can use Pandas value.counts on the appropriate column
# Remember, we are counting how many values there are in the Protocol column

df.groupby(['Protocol']).size().sort_values(ascending=False)
```

**Results**
```bash
Protocol
ICMP    27
DNS     25
HTTP    24
TCP     24
dtype: int64
```

5. Will leave the plot part for you to explore on you own. See you later. Maybe you are a plot person :)

## Brownie Points

1. How many packets were captured (looking at the PacketNumber)?- **100**.

2. What IP address sent the most amount of traffic during the packet capture? - **10.10.1.4**.

3. What was the most frequent protocol? - **ICMP**.
