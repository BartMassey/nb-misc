# Reversal using a stack.
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

from arraystack import Stack

def stack_reverse(l):
    s = Stack(len(l))
    for e in l:
        s.push(e)
    r = []
    while not s.is_empty():
        r.append(s.pop())
    return r

def list_reverse(l):
    r = []
    while l != []:
        r.append(l.pop())
    return r

l = list(range(10))
print(stack_reverse(l))
print(list_reverse(l))
