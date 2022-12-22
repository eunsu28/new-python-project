import os
from time import sleep

def clear():
    return os.system("clear")

def sleep_clear():
    sleep(2)
    clear()

####################################################################
thing = 1

while thing == 1:
    print("this thing will tell you what you've read so far")

    f_input = input("choose the function: ")
    ##########
    if f_input == "a":
        print("add things")
        sleep_clear()
        ##########
        f = open("book.txt", 'a')
        s_input = input(":")
        if s_input == "cancel":
            thing = 2
        f.write("%s\n" %s_input)
        f.close()
        sleep_clear()
    ##########
    elif f_input == "r":
        print("I'll load all the books that you've read")
        sleep_clear()
        f = open("book.txt", 'r')
        read = f.read()
        print(read)
        f.close()
        sleep_clear()
    ##########
    elif f_input == 'f':
        thing = 2
        sleep_clear()


# f = open("book.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()