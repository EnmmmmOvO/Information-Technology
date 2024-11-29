#include <stdlib.h>
#include <stdio.h>

#define TRUE 1
#define FALSE 0
#define BUFF_SIZE 8

int f();

int main(int argv, char **argc) {

    printf("Good luck.\n");
    printf("%p\n", fgets);
    f();
    printf(".\n");

    return EXIT_SUCCESS;
}

int f() {
    char name[BUFF_SIZE];

    printf("> ");
    gets(&name);

    printf("You wrote: %s\n", name);

    return EXIT_SUCCESS;
}
