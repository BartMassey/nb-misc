# Stack class implemented list-style.
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

class Stack(object):

    class StackElement(object):
        def __init__(self, v, rest):
            self.v = v
            self.rest = rest

    def __init__(self):
        self.n = 0
        self.top = None

    def push(self, v):
        old_top = self.top
        self.top = self.StackElement(v, old_top)
        self.n += 1

    def pop(self):
        assert self.n > 0
        v = self.top.v
        self.top = self.top.rest
        self.n -= 1
        return v

    def size(self):
        return self.n

    def is_empty(self):
        return self.size() == 0

if __name__ == "__main__":
    from stacktest import stack_test

    stack_test(Stack)
