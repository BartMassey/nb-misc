/* Copyright © 2014 Bart Massey */
/* Int node methods. */

#include <stdio.h>
#include "int_node.h"

int_node :: int_node(int value, int_node *next) {
    this->value = value;
    this->next = next;
}

void int_node :: print(void) {
    printf("%d\n", this->value);
}
