/* Copyright © 2014 Bart Massey */
/* Linked list node methods. */

#include <stdio.h>
#include "ll_node.h"

ll_node :: ll_node(class ll_elem *value, ll_node *next) {
    this->value = value;
    this->next = next;
}

void ll_node :: print(void) {
    this->value->print();
}
