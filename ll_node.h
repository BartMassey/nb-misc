/* Copyright © 2014 Bart Massey */
/* Linked list node class. */

template <class elem_t>
class ll_node {
public:
    elem_t *value;
    ll_node *next;

    ll_node(elem_t *value, ll_node *next);

    virtual void print(void);
};
