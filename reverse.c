/* Copyright © 2014 Bart Massey */
/* Intlist demo program. */

#include <stdio.h>
#include "intlist.h"

int main(void) {
    int i;
    int a[10];
    struct intlist *lp = 0;

    for (i = 0; i < 10; i++)
        a[i] = i;
    for (i = 0; i < 10; i++)
        intlist_prepend(a[i], &lp);
    intlist_print(&lp);
    intlist_free(&lp);

    printf("\n");

    lp = 0;
    intlist_prepend(5, &lp);
    intlist_prepend(3, &lp);
    intlist_prepend(7, &lp);
    while (lp) {
        int min = intlist_extract_min(&lp);
        printf("%d\n", min);
    }

    return 0;
}
