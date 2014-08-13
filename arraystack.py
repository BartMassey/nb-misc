# Stack class implemented array-style.
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

class Stack(object):

    def __init__(self, max_size):
        if max_size <= 0:
            max_size = 1
        self.stack = [None]*max_size
        self.sp = 0

    def push(self, v):
        if self.sp >= len(self.stack):
            self.stack = self.stack + [None]*len(self.stack)
        self.stack[self.sp] = v
        self.sp += 1

    def pop(self):
        assert self.sp > 0
        self.sp -= 1
        return self.stack[self.sp]

    def size(self):
        return self.sp

    def is_empty(self):
        return self.size() == 0

if __name__ == "__main__":
    from stacktest import stack_test

    stack_test(Stack, 1)
