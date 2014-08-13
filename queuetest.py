# Queue tests.
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

from random import randrange

# Array-based circular queue tests.
def arrayqueuetest(constructor):
    print("base test")
    q = constructor(3)
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
        q = constructor(100)
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
