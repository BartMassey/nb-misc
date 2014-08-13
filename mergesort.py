# Mergesort function
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

def merge(l1, l2):
    r = []
    while len(l1) > 0 and len(l2) > 0:
      if l1[0] <= l2[0]:
        r += [l1[0]]
        l1 = l1[1:]
      else:
        r += [l2[0]]
        l2 = l2[1:]
    return r + l1 + l2

def mergesort(l):
    if len(l) < 2:
        return l
    j = len(l) // 2
    l1 = mergesort(l[:j])
    l2 = mergesort(l[j:])
    return merge(l1, l2)


if __name__ == "__main__":
    from random import randrange
    from time import time

    # Construct a random-length list of random integers.
    def random_list(n, r):
        a = []
        for _ in range(randrange(n)):
            a.append(randrange(r))
        return a

    # Construct a random test list and partition value,
    # and verify that:
    # * The list is properly partitioned, with the correct index returned.
    # * The resulting array is exactly a permutation of the input.
    def test():
        a = random_list(200, 100)
        assert mergesort(a) == sorted(a)

    # Run some random tests.
    print("running tests")
    for _ in range(1000):
        test()
        print(".", end="")
    print()

    # Do some benchmarking on largeish lists.
    for i in range(8):
        n = 10**i
        a = random_list(n, n)
        sa = sorted(a)
        print("testing 10**" + str(i))
        now = time()
        msa = mergesort(a)
        elapsed = (time() - now) / 1000000
        print("tested")
        assert msa == sa
        print("10**" + str(i), elapsed)
