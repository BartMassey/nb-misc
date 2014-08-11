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
    # Number of elements to copy.
    n = j1 - i1
    # If no elements to copy, we're done.
    if n == 0:
        return
    # If source and destination are the same, we're done.
    if i1 == i2:
        return
    # We have to worry about copying right-to-left or
    # left-to-right to avoid clobbering values that we have
    # yet to copy.
    if i2 < i1:
        # Count forward when copying to the left.
        myrange = range(n)
    else:
        # Count backward when copying to the right.
        myrange = range(n-1, -1, -1)
    # Do the copy.
    for i in myrange:
        a[i + i2] = a[i + i1]

# List of test (i1, j1, i2) tuples.
tests = [(3, 6, 7), (3, 6, 4), (3, 6, 2), (0, 4, 2), (2, 6, 4)]

# Run the tests.
for t in tests:
    # Show the test.
    print(t)
    # Make a new array.
    a = list(range(10))
    print(a)
    # Do the copy.
    copy(a, *t)
    print(a)
    # Leave a blank line.
    print()
