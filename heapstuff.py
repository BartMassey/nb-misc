# heap sort, from CLR pp. 142-
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.
# zero-based indexing, top is min

from random import randrange

def exchange(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def checkheap(a, na, i):
    if i < na // 2 - 1:
        assert a[i] >= a[left(i)] and a[i] >= a[right(i)]
        checkheap(a, na, left(i))
        checkheap(a, na, right(i))

def downheap(a, na, i):
    while (right(i) < na):
        xl = a[i] < a[left(i)]
        xr = a[i] < a[right(i)]
        if not xl and not xr:
            break
        xo = a[left(i)] >= a[right(i)]
        if xl and xo:
            exchange(a, i, left(i))
            i = left(i)
            continue
        exchange(a, i, right(i))
        i = right(i)
    if left(i) < na and a[i] < a[left(i)]:
        exchange(a, i, left(i))

def makeheap(a):
    for i in range(len(a) // 2 - 1, -1, -1):
        downheap(a, len(a), i)

def extract_max(a, na):
    exchange(a, 0, na - 1)
    downheap(a, na - 1, 0)
    return a[na - 1]

def heapsort(a):
    makeheap(a)
    for i in range(len(a)):
        v = extract_max(a, len(a) - i)
        a[len(a) - i - 1] = v

def randa():
    a = []
    for _ in range(randrange(2000)):
        a += [randrange(2000)]
    return a

def inorder(a):
    for i in range(len(a)):
        if a[i] != i:
            return False
    return True

def test(a):
    s = sorted(a)
    heapsort(a)
    for i in range(len(a)):
        assert a[i] == s[i]

test([1, 0, 5, 3, 2, 7, 6, 4])
for _ in range(100):
    test(randa())
