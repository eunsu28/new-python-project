import os
from time import sleep

def clear():
    return os.system("clear")


print("this thing will tell you what you've read so far")

a = input("choose the function: ")
if a == "a":
    print("hello")
    sleep(1)
else:
    print("bye")
    sleep(1)

clear()