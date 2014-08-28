/* Copyright © 2014 Bart Massey */
/* Linked list node class. */

template <typename elem_t>
class ll_node {
public:
    elem_t value;
    ll_node *next;

    ll_node(elem_t value, ll_node<elem_t> *next) {
        this->value = value;
        this->next = next;
    }
};
