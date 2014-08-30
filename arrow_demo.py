# Copyright © 2014 Bart Massey
# ASCII CR animation demo.

from time import sleep

width = 40

def arrow_right():

    def print_arrow(i):
        print(" " * i + "->", end="\r")

    print_arrow(0)
    for i in range(1, width - 2):
        sleep(0.1)
        print_arrow(i)

def clear():
    print(end="\r")
    print(" " * width, end="\r")

clear()
arrow_right()
print()
