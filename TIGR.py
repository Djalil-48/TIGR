

import os
import sys
import uncompyle6
from pyfiglet import figlet_format
import base64
from sys import stdout
from time import sleep

E = "\033[1;92m"
K = "\033[1;94m"

class Logo():
    def __init__(self,Logo_run,time):
        self.logo = Logo_run
        self.time = time
        for char in self.logo:
            stdout.write(char)
            stdout.flush()
            sleep(self.time/8)
print(E)
Logo(figlet_format('hamoude',),0.1)

class Uncompyle:
    def decompile_file(self):
        files = input("Enter the name of the file: ")
        if len(files) == 0:
            sys.exit("No file name provided")
        try:
            with open(files, "r") as f:
                bk = f.read()
        except IOError:
            print("File does not exist")
            sys.exit()
        
        try:
            decompiled_code = uncompyle6.main.decompile(3.9, bk)
            with open("decompiled.py", "w") as f:
                f.write(decompiled_code)
            print("Decompilation successful, decompiled code saved in decompiled.py")
        except Exception as e:
            sys.exit("Decompilation failed: {}".format(e))

    def run(self):
        os.system("clear")
        self.decompile_file()

if __name__ == "__main__":
    uncompyle = Uncompyle()
    uncompyle.run()
