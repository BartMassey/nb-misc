/* Copyright © 2014 Bart Massey */
/* Int node class. */

class int_node {
public:
    int value;
    int_node *next;

    int_node(int value, int_node *next);

    virtual void print(void);
};
