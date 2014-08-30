/* Copyright © 2014 Bart Massey */
/* Intlist interface. */

struct intlist {
    int value;
    struct intlist *next;
};

/* intlist.c */
extern void intlist_prepend(int x, struct intlist **lp);
extern void intlist_append(int x, struct intlist **lp);
extern void intlist_free(struct intlist **lp);
extern void intlist_print(struct intlist **lp);
extern int intlist_extract_min(struct intlist **lp);
