/* Copyright © 2014 Bart Massey */
/* Intlist interface. */

struct intlist {
    int value;
    struct intlist *next;
};

/* intlist.c */
extern struct intlist *intlist_prepend(int x, struct intlist *l);
extern struct intlist *intlist_append(int x, struct intlist *l);
extern void intlist_free(struct intlist *l);
extern void intlist_print(struct intlist *l);
extern int intlist_extract_min(struct intlist **lpp);
