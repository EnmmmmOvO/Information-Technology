#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char correct_password[32] = "(,\x00\x13\n#\x18\x33\x0e\r\r\x08\x0f\x06%PQQ\x12\x6b\x61";

void win(void) {
    char flag[64];

    FILE *fp = fopen("flag", "r");
    if (fp == NULL) {
        printf("flag file not found\n");
        return;
    } else {
        fgets(flag, 64, fp);
    }

    printf("%s\n", flag);
}

int vuln(int canary) {
    int read_only = 1;
    int canary_cpy = canary;
    char student_name[64];
    memset(student_name, 0, 64);

    printf("COMP6[48]41 SAP Marking Server\n");
    printf("[debug] Canary value: 0x%08x\n", canary);

    char password[32];
    memset(password, 0, 32);

    printf("Enter password:\n");
    fgets(password, 32, stdin);

    for (int i = 0; i < 32; i++) {
        correct_password[i] = correct_password[i] ^ 97;
    }

    if (strncmp(password, correct_password, 32)) {
        printf("Wrong password. This incident will be reported.\n");
        return 1;
    }

    printf("Enter student's name: ");
    fgets(student_name, 69, stdin);

    if (read_only) {
        printf("That student's mark is %d.\n", rand() % 100);
    } else {
        if (canary != canary_cpy) {
            printf("[fatal] Security breach! Re-randomising marks...\n");
            return 1;
        }
        win();
    }

    return 0;
}

int main(void) {
    setbuf(stdout, NULL);
    srand(time(NULL));
    int canary = rand();
    vuln(canary);
}
