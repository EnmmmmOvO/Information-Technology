// COMP9315 22T1 Final Exam Q1
// Find longest tuple in a no-frills file

#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include "no-frills.h"

int main(int argc, char **argv)
{
	if (argc < 2) {
		printf("Usage: %s DataFile\n", argv[0]);
		exit(1);
	}
	int fd = open(argv[1],O_RDONLY);
	if (fd < 0) {
		printf("Can't open file %s\n", argv[1]);
		exit(1);
	}
	char longest[MAXTUPLEN];

	// Add variables and code here to find
	// the longest tuple in the data file

	int pages = 0;
	int len = 0;
	char temp[PAGESIZE];
	int nd = 0;

	while((nd = read(fd, temp, PAGESIZE)) == PAGESIZE) {
		char *i = temp;
		while (1) {
			int length = strlen(i);
			
			if (length == 0) break;

			if (len < length) {
				len = length;
				strcpy(longest, i);
			}

			i += length + 1;
		}
		pages++;
	}


	if (pages == 0 || len == 0 || (nd > 0 && nd < PAGESIZE)) {
		sprintf(longest, "<none>");
	}

	printf("%s\n",longest);
	return 0;
}
