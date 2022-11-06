import os
from time import sleep

thing = 1

def clear():
    return os.system("clear")

while thing:
    print("this thing will tell you what you've read so far")
    
    f_input = input("choose the function: ")
    if f_input == "a":
        print("add things")
        sleep(1)
        f = open("book.txt", 'a')
        s_input = input(":")
        f.write("%s\n" %s_input)
        f.close()
    elif f_input == "r":
        print("bye")
        sleep(1)

    clear()