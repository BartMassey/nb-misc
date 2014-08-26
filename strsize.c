/* Copyright © 2014 Bart Massey */
/* String size demo. */

#include <stdio.h>
#include <string.h>

int mystrlen(char *s) {
    int i = 0;

    while (s[i] != '\0') {
        i++;
    }
    return i;
}

int main(void) {
    char *hello = "hello";

    printf("%lu\n", sizeof(hello));
    printf("%d\n", mystrlen(hello));
    printf("%lu\n", strlen(hello));
    printf("%d\n", hello[5]);
    return 0;
}
