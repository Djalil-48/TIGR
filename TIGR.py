import os

# Banner
banner = """
\033[1;31m   d8888b.  d8888b. d8888b. 
\033[1;32m   88  `8D  88  `8D 88  `8D 
\033[1;33m   88oobY'  88oooY' 88oooY' 
\033[1;34m   88`8b    88~~~b. 88~~~b. 
\033[1;35m   88 `88.  88   8D 88   8D 
\033[1;36m   88   YD  Y8888P' Y8888P' 
\033[1;32m             TIGR TOOL  
"""

info = """
\033[1;32m[-] AUTHOR   : DJALIL
[-] TOOL     : TIGR
[-] VERSION  : 1.0
"""

menu = """
\033[1;31m[1] OPTION ONE
[2] OPTION TWO
[0] EXIT
"""

os.system("clear")
print(banner)
print(info)
print(menu)

choose = input("\033[1;32m[-] CHOOSE : ")

if choose == "1":
    print("\033[1;33mYOU SELECTED OPTION ONE")

elif choose == "2":
    print("\033[1;34mYOU SELECTED OPTION TWO")

elif choose == "0":
    print("\033[1;31mEXITING...")

else:
    print("\033[1;31mINVALID OPTION!")
