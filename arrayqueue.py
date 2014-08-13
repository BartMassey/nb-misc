# Array-based circular queue implementation.
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

class Queue(object):
    def __init__(self, max_size):
        self.queue = [None] * (max_size + 1)
        self.enq = 0
        self.deq = 0
        self.n = 0

    def increase(self, n):
        n += 1
        if n >= len(self.queue):
            n -= len(self.queue)
        return n

    def enqueue(self, v):
        assert not self.is_full()
        self.queue[self.enq] = v
        self.enq = self.increase(self.enq)
        self.n += 1

    def dequeue(self):
        assert not self.is_empty()
        v = self.queue[self.deq]
        self.deq = self.increase(self.deq)
        self.n -= 1
        return v

    def is_empty(self):
        assert (self.enq == self.deq) == (self.n == 0)
        return self.n == 0

    def is_full(self):
        return self.increase(self.enq) == self.deq

    def size(self):
        return self.n

if __name__ == "__main__":
    from random import randrange

    print("base test")
    q = Queue(3)
    assert q.is_empty()
    assert not q.is_full()
    q.enqueue(1)
    assert not q.is_empty()
    assert not q.is_full()
    q.enqueue(2)
    assert not q.is_empty()
    assert not q.is_full()
    q.enqueue(3)
    assert not q.is_empty()
    assert q.is_full()
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty()

    def test():
        q = Queue(100)
        v = 1
        w = 1
        for _ in range(randrange(100) + 1):
            q.enqueue(v)
            v += 1
        while True:
            if randrange(2) == 1:
                if q.is_full():
                    break
                q.enqueue(v)
                v += 1
            else:
                if q.is_empty():
                    break
                assert q.dequeue() == w
                w += 1

    print("random tests")
    for _ in range(100):
        test()
        print(".", end="")
    print()
