/* Copyright © 2014 Bart Massey */
/* Fibonacci Numbers via recursion. */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

int fib(int n) {
    if (n == 0 || n == 1)
        return 1;
    return fib(n - 2) + fib(n - 1);
}

int main(int argc, char *argv[]) {
    int n;

    assert(argc == 2);
    n = atoi(argv[1]);
    assert(n > 0);
    printf("%d\n", fib(n));
    return 0;
}
