# Copyright © 2014 Bart Massey
# Function to copy elements of an array around.

# Copy elements of array a starting at
# i1 and ending just before j1. After
# the copy, these elements should
# reside starting at i2. Invariant:
# there should be sufficient space after i2
# for the copy to complete. Optional invariant:
# Copied elements should also be preserved in
# the source position where possible.
def copy(a, i1, j1, i2):
    if j1 == i1:
        return
    if i1 == i2:
        return
    if i2 < i1:
        myrange = range(i1, j1)
    else:
        myrange = range(j1-1, i1-1, -1)
    for i in myrange:
        a[i2 + (i - i1)] = a[i]

tests = [(3, 6, 7), (3, 6, 4), (3, 6, 2), (0, 4, 2), (2, 6, 4)]
for t in tests:
    print(t)
    a = list(range(10))
    print(a)
    copy(a, *t)
    print(a)
    print()
