#include <stdlib.h>
#include <stdio.h>
#include "printFlag.c"

#define TRUE 0
#define FALSE -1
#define BUFF_SIZE 16

int printName();

int main(int argv, char **argc) {

    printf("Welcome!\n");
    printName();
    printf("Everything is good.\n");

    return EXIT_SUCCESS;
}

int printName() {
    int isAdmin = FALSE;
    char name[BUFF_SIZE];

    printf("What is your name?\n");

    printf("> ");
    fgets(&name, BUFF_SIZE+1, stdin); // Size of buffer plus the null terminator

    if (isAdmin == FALSE) {
        printf("Welcome, %s!\n", name);
        printf("You are in this program, but we do not grant you the rank of Admin.\n");
        printf("Now go away, or I will taunt you a second time.\n");
    } else {
        printf("Welcome, %s!\n", name);
        printf("With great power comes great responsibility...\n");
        printFlag();
    }
    return EXIT_SUCCESS;
}
