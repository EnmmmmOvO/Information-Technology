#include <stdlib.h>
#include <stdio.h>

#define FLAG_SIZE 64

int printFlag() {
    // Defining file pointer and opening the file.
    FILE *file_ptr;
    char str[FLAG_SIZE];

    file_ptr = fopen("flag.txt", "r");

    // Check if flag file exists
    if (file_ptr == NULL) {
        printf("Your payload worked! Your are admin.\n");
        printf("There is no flag file. If you're seeing this locally, that's okay. Try a remote exploit. If you're seeing this remotely, please contact the admin.\n");
    }

    // Reading stinrg using fgets
    printf("Here is your flag:\n");
    while (fgets(str, FLAG_SIZE, file_ptr) != NULL) {
        printf("%s", str);
    }

    fclose(file_ptr);
    return EXIT_SUCCESS;
}
