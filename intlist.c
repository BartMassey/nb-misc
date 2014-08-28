/* Copyright © 2014 Bart Massey */
/* Linked lists of ints. */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "intlist.h"

void intlist_prepend(int x, struct intlist **lp) {
    struct intlist *xl = malloc(sizeof *xl);
    assert(xl);
    xl->value = x;
    xl->next = *lp;
    *lp = xl;
}

void intlist_append(int x, struct intlist **lp) {
    struct intlist *xl = malloc(sizeof *xl);
    assert(xl);
    xl->value = x;
    xl->next = 0;
    while (*lp)
        lp = &((*lp)->next);
    *lp = xl;
}

void intlist_free(struct intlist **lp) {
    while (*lp) {
        struct intlist **saved_lp = &(*lp)->next;
        free(*lp);
        lp = saved_lp;
    }
    /* XXX Just for "safety". */
    *lp = 0;
}

void intlist_print(struct intlist **lp) {
    for(; *lp; lp = &((*lp)->next)) {
        printf("%d\n", (*lp)->value);
    }
}

int intlist_extract_min(struct intlist **lp) {
    int min;
    struct intlist **min_lp;
    struct intlist *saved_l;
    
    assert(*lp);
    min = (*lp)->value;
    min_lp = lp;
    for (; *lp; lp = &((*lp)->next)) {
        if ((*lp)->value < min) {
            min = (*lp)->value;
            min_lp = lp;
        }
    }

    saved_l = (*min_lp)->next;
    free(*min_lp);
    *min_lp = saved_l;
    return min;
}
