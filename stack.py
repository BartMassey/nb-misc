# Copyright © 2014 Bart Massey
# Stack class implemented list-style.

class StackElement(object):
    def __init__(self, v, rest):
        self.v = v
        self.rest = rest

class Stack(object):
    def __init__(self):
        self.n = 0
        self.top = None

    def push(self, v):
        old_top = self.top
        self.top = StackElement(v, old_top)
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

    from random import randrange

    def test():
        a = []
        for _ in range(randrange(100)):
            a += [randrange(100)]
        n = len(a)
        s = Stack()
        i = n // 2
        for j in range(i):
            s.push(a[j])
        while i > 0:
            if s.size() < n - 1 and randrange(2) == 1:
                s.push(a[i])
                i += 1
                assert s.size() == i
                assert not s.is_empty()
            else:
                v = s.pop()
                i -= 1
                assert v == a[i]
                assert s.size() == i
        assert s.is_empty()

    for _ in range(100):
        test()
        print(".", end="")
    print()
