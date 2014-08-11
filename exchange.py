# Copyright © 2014 Bart Massey
# Function to exchange elements in an array.

# Exchange elements i and j of array a.
def exchange(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp

a = [1, 2]
exchange(a, 0, 1)
print(a)
