# Copyright © 2014 Bart Massey
# Print the hex value of the set of vowels.

n = 0
for c in ('a', 'e', 'i', 'o', 'u'):
    b = 2**(ord(c) - ord('a'))
    n += b
print(format(n, "x"))
