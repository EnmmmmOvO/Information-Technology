#include <stdlib.h>
#include <stdio.h>

#define TRUE 1
#define FALSE 0
#define BUFF_SIZE 512

int printName();

int main(int argv, char **argc) {

    printf("Welcome!\n");
    printName();
    printf("Everything is good.\n");

    return EXIT_SUCCESS;
}

int printName() {
    char name[BUFF_SIZE];

    printf("Your buffer is located at: %p\n", name);

    printf("What is your name?\n");
    printf("> ");
    gets(&name);

    printf("Welcome, %s!\n", name);

    return EXIT_SUCCESS;
}
