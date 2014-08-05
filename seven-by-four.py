# Copyright © 2014 Bart Massey
# Check that Pr(E|H) = 1/6 where:
# E is the event of rolling a four on two dice.
# H is the event of having one of the dice a four.

from random import randrange

num_fourdie = 0
num_seven_by_fourdie = 0

for _ in range(100000):
    (d1, d2) = (randrange(1, 7), randrange(1, 7))
    if d1 != 4 and d2 != 4:
        continue
    num_fourdie += 1
    if d1 + d2 != 7:
        continue
    num_seven_by_fourdie += 1

print(num_seven_by_fourdie, num_fourdie, num_seven_by_fourdie / num_fourdie)
