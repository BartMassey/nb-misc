/* Copyright © 2014 Bart Massey */
/* Linked list node methods. */

#include <stdio.h>
#include "ll_node.h"

template <class elem_t>
ll_node<elem_t> :: ll_node(elem_t *value, ll_node *next) {
    this->value = value;
    this->next = next;
}

template <class elem_t>
void ll_node<elem_t> :: print(void) {
    this->value->print();
}
