/* Copyright © 2014 Bart Massey */
/* Intlist demo program. */

#include "intlist.h"

int main(void) {
    int i;
    int a[10];
    struct intlist *lp = 0;

    for (i = 0; i < 10; i++)
        a[i] = i;
    for (i = 0; i < 10; i++)
        lp = intlist_prepend(a[i], lp);
    intlist_print(lp);
    intlist_free(lp);
    return 0;
}
