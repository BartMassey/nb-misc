# Copyright © 2014 Bart Massey
# Partition an array around a pivot.

# Rearrange a such that all elements less than k precede all
# elements >= k. Return the index just after the last
# less-than element.
def partition(a, k):
    n = len(a)
    l = 0
    u = n - 1
    while True:
        while l < n and a[l] < k:
            l += 1
        while u >= 0 and a[u] >= k:
            u -= 1
        if l >= u:
            return l
        tmp = a[l]
        a[l] = a[u]
        a[u] = tmp

if __name__ == "__main__":
    from random import randrange

    # Construct a random test list and partition value,
    # and verify that:
    # * The list is properly partitioned, with the correct index returned.
    # * The resulting array is exactly a permutation of the input.
    def test():
        k = randrange(50)
        a = []
        for _ in range(randrange(20)):
            a.append(randrange(100))
        aa = sorted(a)
        p = partition(a, k)
        for i in range(p):
            assert a[i] < k
        for i in range(p, len(a)):
            assert a[i] >= k
        assert sorted(a) == aa

    # Run some random tests.
    for i in range(10000):
        test()
