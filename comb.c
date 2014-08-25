/* Copyright © 2014 Bart Massey */
/* Combinatorics functions. */

#include "comb.h"

int factorial(int n) {
    if (n == 0)
        return 1;
    return n * factorial(n - 1);
}

int product(int i, int j) {
    int k;
    int result = i;

    for (k = i + 1; k <= j; k++)
        result *= k;
    return result;
}

int choose(int n, unsigned short k) {
    if (k > n - k)
        k = n - k;
    return product(n - k + 1, n) / factorial(k);
}
