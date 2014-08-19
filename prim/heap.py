# Heap stuff in Python for New Beginnings
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i + 1) // 2 - 1

def exchange(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

class Heap(object):
    def __init__(self, max_occupancy):
        self.n = 0
        self.a = [0] * max_occupancy

    def downheap(self, i):
        # Find indices of possible children.
        l = left(i)
        r = right(i)
        # Leaf case.
        if l >= self.n:
            return
        # Left child only case.
        if r >= self.n:
            if self.a[l] < self.a[i]:
                exchange(self.a, i, l)
            return
        # Case in which no more adjustment is needed.
        if self.a[i] <= self.a[l] and self.a[i] <= self.a[r]:
            return
        # Case in which we must adjust.
        if self.a[l] < self.a[r]:
            # Case in which we push left.
            exchange(self.a, i, l)
            self.downheap(l)
        else:
            # Case in which we must push right.
            exchange(self.a, i, r)
            self.downheap(r)

    def extract_min(self):
        assert self.n > 0
        # The root of the heap is the minimum value.
        m = self.a[0]
        # Decrease the heap size by 1 to account for the extraction.
        self.n -= 1
        # If the heap is empty, we're done.
        if self.n == 0:
            return m
        # Set the root to the former last value.
        self.a[0] = self.a[self.n]
        # Reinstate the heap property.
        self.downheap(0)
        # Return the extracted value.
        return m

    def upheap(self, i):
        # If we're at the root, stop.
        if i == 0:
            return
        p = parent(i)
        # Heap invariant reinstated, so quit.
        if self.a[p] <= self.a[i]:
            return
        # Fix the parent.
        exchange(self.a, i, p)
        self.upheap(p)

    def insert(self, value):
        assert self.n < len(self.a)
        # Store the value.
        self.a[self.n] = value
        # Mark it as used.
        self.n += 1
        # Reinstate the heap property.
        self.upheap(self.n - 1)


if __name__ == "__main__":
    from random import randrange

    print("Hardwired extract_min test.")
    h = Heap(0)
    h.n = 7
    h.a = [0, 2, 1, 4, 7, 3, 5]
    r = []
    for _ in range(h.n):
        r += [h.extract_min()]
    print(r)
    assert r == [0, 1, 2, 3, 4, 5, 7]

    def insert_test():
        h = Heap(100)
        a = []
        for _ in range(randrange(100)):
            a += [randrange(100)]
        for v in a:
            h.insert(v)
        l1 = sorted(a)
        l2 = []
        for _ in range(len(a)):
            l2 = l2 + [h.extract_min()]
        assert l1 == l2

    print("Random insert/extract-min test.")
    for _ in range(100):
        insert_test()
        print(".", end="")
    print()
