/* Copyright © 2014 Bart Massey */
/* Int list implementation. */

#include "ll_node.h"

template <typename elem_t>
class ll {
    ll_node<elem_t> *head;

public:
    ll(void) {
        this->head = 0;
    }

    void prepend(elem_t value) {
        this->head = new ll_node<elem_t>(value, this->head);
    }

    void traverse(void (*tf)(elem_t)) {
        for (ll_node<elem_t> *lp = this->head; lp; lp = lp->next)
            tf(lp->value);
    }
};
