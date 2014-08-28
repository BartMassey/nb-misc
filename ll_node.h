/* Copyright © 2014 Bart Massey */
/* Linked list node class. */

class ll_elem {
public:
    virtual void print(void) = 0;
    virtual int compare(class ll_elem *e) = 0;
};

class int_ll_elem : ll_elem {
    int value;

public:
    int_ll_elem(int value) {
        this->value = value;
    }

    virtual void print(void) {
        printf("%d\n", this->value);
    }

    virtual int compare(class int_ll_elem *e) {
        return this->value <= e->value;
    }
};

class ll_node {
public:
    class ll_elem *value;
    ll_node *next;

    ll_node(class ll_elem *value, ll_node *next);

    virtual void print(void);
};
