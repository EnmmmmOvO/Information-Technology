// COMP9315 22T1 Final Exam Q1
// Count tuples in a no-frills file

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
	int ntuples = 0;

	// Add variables and code here to work out
	// the total number of tuples

	char temp[PAGESIZE];
	int nd;
	int page = 0;

	while ((nd = read(fd, temp, PAGESIZE)) == PAGESIZE) {
		ntuples += temp[0];
		page ++;
	}

	if (page == 0 || (nd > 0 && nd < PAGESIZE)) {
		ntuples = -1;
	}

	printf("%d\n",ntuples);
	return 0;
}
