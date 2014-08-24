# Copyright © 2014 Bart Massey
# Fibonacci Numbers via recursion.

from sys import argv

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)

assert len(argv) == 2
n = int(argv[1]);
assert n > 0
print(fib(n))
