#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "printFlag.c"

#define TRUE 1
#define FALSE 0

int r;

int printName();

int main(int argv, char **argc) {

    srand(time(NULL));      // Initialization, should only be called once.
    r = rand();             // Returns a pseudo-random integer between 0 and RAND_MAX.

    printf("Welcome!\n");
    printName();
    printf("Everything is good.\n");

    return EXIT_SUCCESS;
}

int printName() {
    int isAdmin = FALSE;
    int CANARY = r;
    char name[16];

    printf("The canary is %d\n", CANARY);
    printf("What is your name?\n");
    printf("> ");
    gets(&name);

    if (isAdmin == FALSE) {
        printf("Welcome, %s!\n", name);
        printf("You are in this program, but we do not grant you the rank of Admin.\n");
        printf("Now go away, or I will taunt you a second time.\n");

        return EXIT_SUCCESS;
    } else {
        // Check the canary
        if (CANARY != r) {
            printf("You're not the messiah! You're a very naughty student!");
            return EXIT_FAILURE;
        } else {
            printf("Welcome, %s!\n", name);
            printf("With great power comes great responsibility...\n");
            printFlag();

            return EXIT_SUCCESS;
        }
    }
}
