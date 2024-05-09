// COMP9315 22T1 Final Exam Q3
// Read tuples from stdin and store in no-frills file
// Start from empty file, add new pages as needed

#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include "no-frills.h"

void create_new_page(char *page, char **local, int *large);
void write_page(char *page, int fd);

int main(int argc, char **argv)
{
	if (argc < 3) {
		fprintf(stderr, "Usage: %s DataFile TupleFile\n", argv[0]);
		exit(1);
	}
	unsigned int mode = S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH;
	int fd = open(argv[1],O_RDWR|O_CREAT|O_TRUNC,mode);
	if (fd < 0) {
		fprintf(stderr, "Can't open data file.\n");
		exit(1);
	}
	FILE *input = fopen(argv[2],"r");
	if (input == NULL) {
		fprintf(stderr, "Can't open data file.\n");
		exit(1);
	}

	// Add variables and code here to read tuples from
	// input and append them to the "no-frills" file

	char *local = NULL;
	int large = 0;
	char page[PAGESIZE];
	char i[PAGESIZE];

	create_new_page(page, &local, &large);

	while(fgets(i, PAGESIZE, input) != NULL) {
		int len = strlen(i);

		if (large < len || page[0] > MAXTUPLEN) {
			write_page(page, fd);
			create_new_page(page, &local, &large);
		}

		i[len - 1] = '\0';

		if (page[0] == '\0') page[0] = 1; else page[0]++;
		strcpy(local, i);

		local += len;
		large -= len;
	} 

	write_page(page, fd);

	return 0;
}

void create_new_page(char *page, char **local, int *large) {
	memset(page, '\0', PAGESIZE);
	*local = page + 1;
	*large = PAGESIZE - 3;
}

void write_page(char *page, int fd) {
	write(fd, page, PAGESIZE);
}