import os
from time import sleep

def clear():
    return os.system("clear")

####################################################################
thing = 1

while thing == 1:
    print("this thing will tell you what you've read so far")

    f_input = input("choose the function: ")
    ##########
    if f_input == "a":
        print("add things")
        sleep(1)
        ##########
        f = open("book.txt", 'a')
        s_input = input(":")
        if s_input == "cancel":
            thing = 2
        f.write("%s\n" %s_input)
        f.close()
    ##########
    elif f_input == "r":
        print("I'll load all the books that you've read")
        sleep(1)
        f = open("book.txt", 'r')
        while True:
            line = f.readline()
            if not line: break
            print(line)
        f.close()
    ##########
    elif f_input == 'f':
        thing = 2
        clear()