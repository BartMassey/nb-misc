# Copyright © 2014 Bart Massey
# Primality tester

from math import sqrt, floor

# Return True if n is prime, false otherwise.
def prime_check(n):
    # Two is prime.
    if n == 2:
        return True

    # Even numbers are composite.
    if n % 2 == 0:
        return False

    # Walk the odd numbers that are possible factors
    # of n looking for a hit.
    for d in range(3, floor(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False

    # No factors were found, so n is prime.
    return True

candidate = int(input("candidate prime? "))
if prime_check(candidate):
    print("prime")
else:
    print("composite")
