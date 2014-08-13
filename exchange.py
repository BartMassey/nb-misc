# Function to exchange elements in an array.
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# Exchange elements i and j of array a.
def exchange(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp

a = [1, 2]
exchange(a, 0, 1)
print(a)
