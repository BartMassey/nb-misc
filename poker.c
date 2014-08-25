/* Copyright © 2014 Bart Massey */
/* Poker hand statistics. */

#include <stdio.h>
#include "comb.h"

int main(void) {
    printf("number of pairs in a 5-unique card hand = %d\n",
           choose(5, 2));
    printf("number of 5-card poker hands = %d\n",
           choose(52, 5));
    printf("number of 5-card poker hands "
           "with at least one pair = %d\n",
           13 * choose(4, 2) * choose(50, 3));
    return 0;
}
