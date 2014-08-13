# Stack test class.
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

from random import randrange

def stack_test(stack_constructor, *args):
    def test():
        a = []
        for _ in range(randrange(100)):
            a += [randrange(100)]
        n = len(a)
        s = stack_constructor(*args)
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
