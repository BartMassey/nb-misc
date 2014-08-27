/* Copyright © 2014 Bart Massey */
/* Int list method implementations. */

#include "int_list.h"

int_list :: int_list(void) {
    this->head = 0;
}

void int_list :: prepend(int value) {
    this->head = new int_node(value, this->head);
}

void int_list :: print(void) {
    for (int_node *lp = this->head; lp; lp = lp->next)
        lp->print();
}
