/* Copyright © 2014 Bart Massey */
/* intlist demo */

#include <stdio.h>

class int_node {
public:
    int value;
    int_node *next;

    int_node(int value, int_node *next) {
        this->value = value;
        this->next = next;
    }

    virtual void print(void) {
        printf("%d\n", this->value);
    }
};


class int_list {
    int_node *head;

public:
    int_list(void) {
        this->head = 0;
    }

    virtual void prepend(int value) {
        this->head = new int_node(value, this->head);
    }

    virtual void print(void) {
        int_node *lp;
        for (lp = this->head; lp; lp = lp->next)
            lp->print();
    }
};

int main(void) {
    int i;
    int_list l;
    for (i = 0; i < 10; i++)
        l.prepend(i);
    l.print();
    return 0;
}
