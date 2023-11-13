"""
Solution for the Pico CTF 2K21 General Skill Challenge - Nice netcat....

Description: There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 35652, but it doesn't speak English...

Solution: The program speaks ASCII. Let's get them to char and print the message.

Flag: picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}
"""


def main():
    f = open("/home/kali/Desktop/Git_work/CTF/PICO CTF/2K21/GS/Nice netcat/netcat.txt", "r")
    input = f.readlines()

    flag = ""
    for i in input:
        flag += chr(int(i))
    print(flag)

if __name__ == "__main__":
    main()