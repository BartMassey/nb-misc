/* Copyright © 2014 Bart Massey */
/* Int list implementation. */

#include "int_node.h"

class int_list {
    int_node *head;

public:
    int_list(void);

    virtual void prepend(int value);

    virtual void print(void);
};
