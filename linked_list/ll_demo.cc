/* Copyright © 2014 Bart Massey */
/* Linked list demo. */

#include <stdio.h>
extern "C" {
#include "intlist.h"
}
#include "ll.h"

class int_list_adapter {
    struct intlist *head;

public:
    int_list_adapter(void) {
        head = 0;
    }

    virtual void prepend(int v) {
        intlist_prepend(v, &head);
    }

    virtual void append(int v) {
        intlist_append(v, &head);
    }

    ~int_list_adapter(void) {
        intlist_free(&head);
    }

    virtual void print(void) {
        intlist_print(&head);
    }

    virtual int extract_min(void) {
        return intlist_extract_min(&head);
    }
};

void print(int v) {
    printf("%d\n", v);
}

int main(void) {
    ll<int> l;
    for (int i = 0; i < 10; i++)
        l.prepend(i);
    l.traverse(print);

    printf("\n");

    int_list_adapter al;
    for (int i = 0; i < 10; i++)
        al.prepend(i);
    al.print();

    return 0;
}
