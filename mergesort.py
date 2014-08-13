# Copyright © 2014 Bart Massey
# Mergesort function

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
    l1 = mergesort(l[0:j])
    l2 = mergesort(l[j:])
    return merge(l1, l2)


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
        aa = a[:]
        assert mergesort(a) == sorted(aa)

    # Run some random tests.
    for _ in range(10000):
        test()
