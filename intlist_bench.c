/* Copyright © 2014 Bart Massey */
/* Intlist benchmarks. */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "intlist.h"

int main(int argc, char **argv) {
    int n, i;
    struct intlist *l;

    assert(argc == 2);
    n = atoi(argv[1]);
    assert(n > 0);
    srandom(100);

    l = 0;
    for (i = 0; i < n; i++) {
        intlist_prepend(random(), &l);
    }

    intlist_free(&l);

    l = 0;
    for (i = 0; i < n; i++) {
        intlist_append(random(), &l);
    }

    int min = intlist_extract_min(&l);
    for (i = 1; i < n; i++) {
        int m = intlist_extract_min(&l);
        assert(m >= min);
        min = m;
    }

    return 0;
}
