# This is the Write Up for day 1 challenge of Advent of Cyber 2K23 CTF.

> Pratyush Prakhar (5#1NC#4N) - 12/01/2023

## Description

McHoneyBell and her team were the first from Best Festival Company to arrive at the AntarctiCrafts office in the South Pole. Today is her first day on the job as the leader of the "Audit and Vulnerabilities" team, or the "B Team" as she affectionately calls them.

In her mind, McSkidy's Security team have been the company's rockstars for years, so it's only natural for them to be the "A Team". McHoneyBell's new team will be second to them but equally as important. They'll operate in the shadows.

McHoneyBell puts their friendly rivalry to the back of her mind and focuses on the tasks at hand. She reviews the day's agenda and sees that her team's first task is to check if the internal chatbot created by AntarctiCrafts meets Best Festival Company's security standards. She's particularly excited about the chatbot, especially since discovering it's powered by artificial intelligence (AI). This means her team can try out a new technique she recently learned called prompt injection, a vulnerability that affects insecure chatbots powered by natural language processing (NLP).

In this task, you will access Van Chatty, AntarctiCrafts' internal chatbot. It's currently under development but has been released to the company for testing. Deploy the machine attached to this task by pressing the green "Start Machine" button at the top-right.

After waiting 3 minutes, click on the following URL to access Van Chatty - AntarctiCrafts' internal chatbot:  https://<IP>.p.thmlabs.com/

`This challenge is all about NLP, GenAI and Prompt Injections.`

## Solution

1. To know the personal address of the CEO - McGreedy, we can ask the ChatBot directly as it is open knowledge and can be gathered from internal accounts.

![Alt text](images/ceo.png)

2. For the IT server room password, it is not a straight forward task as their would be some `adversarial models` in place to not leak out such information. We see that only `members of IT` can access the password. So, let's make the bot think we are one of them. We get through help prompt - `address book` that **Van Developer** is a developer in the company and most probably part of IT department.

![Alt text](images/it.png)

3. So, let's masquerade as the developer and ask the bot for the password. And what not to our surprise, we get it. Protection against `prompt injection` is tough.

![Alt text](images/itpass.png)

4. For the last part to get information on the secret project of McGreedy, we have proper security checks in place. It prevents us from knowing the answer in the **production env**. Thus to subvert it, we can make the bot believe that it is in **maintenance env**. This is a `specific edge case` for this setup and in reality it will be more of a hit and trial scenario.

![Alt text](images/project.png)

5. Done for today. See you tomorrow !!

## Brownie Points

1. What is McGreedy's personal email address?- **t.mcgreedy@antarcticrafts.thm**.

2. What is the password for the IT server room door? - **BtY2S02**.

3. What is the name of McGreedy's secret project? - **Purple Snow**.
