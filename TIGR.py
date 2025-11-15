import os
import time
import sys

# شاشة تحميل وهمية مثل git clone
os.system("clear")
for i in range(1, 101):
    sys.stdout.write(f"\rReceiving objects: {i}% ( {i}/100 ), 5.32 MiB | 1.{i} MiB/s")
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1)
print("\nAlready up to date.\n")
time.sleep(1)

os.system("clear")

# هنا تبدأ أداتك الأصلية
print("""
████████ TIGR ████████

[1] START TOOL
[2] ABOUT
[0] EXIT
""")

import os
import time

# Colors
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
W = "\033[1;37m"

def banner():
    os.system("clear")
    print(R + """
████████╗██╗ ██████╗ ██████╗ 
╚══██╔══╝██║██╔════╝██╔═══██╗
   ██║   ██║██║     ██║   ██║
   ██║   ██║██║     ██║   ██║
   ██║   ██║╚██████╗╚██████╔╝
   ╚═╝   ╚═╝ ╚═════╝ ╚═════╝  
""")
    print(G + "[-] FACEBOOK : DJALIL mk")
    print(G + "[-] TELEGRAM : djalil_dz_48")
    print(G + "[-] AUTHOR   : DJALIL")
    print(G + "[-] TOOL     : TIGR")
    print(G + "[-] VERSION  : 1.0.0")
    print(B + "----------------------------------------\n")

def menu():
    print(G + "[1] FILE CLONING")
    print(G + "[2] FOLLOW FB")
    print(G + "[3] TOOL INFO")
    print(R + "[0] EXIT\n")
    return input(Y + "[-] CHOOSE : " + W)

def file_cloning():
    os.system("clear")
    print(C + "[*] FILE CLONING MODULE COMING SOON...")
    time.sleep(2)

def follow_fb():
    os.system("xdg-open https://facebook.com/")
    print(G + "[*] OPENED FACEBOOK")
    time.sleep(2)

def tool_info():
    os.system("clear")
    print(G + "[*] TIGR TOOL CREATED BY DJALIL")
    print(G + "[*] VERSION 1.0.0")
    print(G + "[*] MADE WITH ❤️")
    time.sleep(3)

while True:
    banner()
    option = menu()

    if option == "1":
        file_cloning()

    elif option == "2":
        follow_fb()

    elif option == "3":
        tool_info()

    elif option == "0":
        print(R + "[!] EXITING...")
        time.sleep(1)
        break

    else:
        print(R + "[!] INVALID OPTION")
        time.sleep(1)
