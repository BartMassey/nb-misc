# Copyright © 2014 Bart Massey
# ASCII CR animation demo.

from time import sleep

width = 20

def clear():
    print(end="\r")
    print(" " * width, end="\r")

def display_animation(figure, positions):

    def display_frame(i):
        print(" " * i + figure, end="\r")

    for i in positions:
        sleep(1/20)
        clear()
        display_frame(i)

def animation_move_right(figure):
    display_animation(figure, range(width - len(figure) + 1))

def animation_move_left(figure):
    display_animation(figure, range(width - len(figure), -1, -1))

for figs in [("->", "<-"), ("=>", "<=")]:
    animation_move_right(figs[0])
    animation_move_left(figs[1])

print()
