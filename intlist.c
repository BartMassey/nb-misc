/* Copyright © 2014 Bart Massey */
/* Linked lists of ints. */

#include <stdio.h>
#include <stdlib.h>
#include "intlist.h"

struct intlist *intlist_prepend(int x, struct intlist *l) {
    struct intlist *xl = malloc(sizeof *xl);
    (*xl).value = x;
    (*xl).next = l;
    return xl;
}

struct intlist *intlist_append(int x, struct intlist *l) {
    struct intlist *lp;
    struct intlist *xl = malloc(sizeof *xl);
    (*xl).value = x;
    (*xl).next = 0;
    if (!l)
        return xl;
    lp = l;
    while (lp->next)
        lp = lp->next;
    lp->next = xl;
    return l;
}

void intlist_free(struct intlist *l) {
    while (l) {
        struct intlist *lp = l->next;
        free(l);
        l = lp;
    }
}

void intlist_print(struct intlist *l) {
    while (l) {
        printf("%d\n", l->value);
        l = l->next;
    }
}
