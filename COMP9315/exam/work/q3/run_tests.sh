#!/bin/sh

if [ ! -d "tests" ]
then
	echo "You must run this script from your 'q3' directory"
	exit 1
fi

if [ ! -x "q3" ]
then
	echo "You don't seem to have a program to test"
	exit 1
fi

for t in 01 02 03 04 05
do
	tt="tests/$t"
	sh $tt.sh 2>&1 | head -n200 > $tt.observed
	diff -wi $tt.expected $tt.observed > $tt.diffs

	echo ""
	echo "===== Test $t ====="
	if [ ! -s "$tt.diffs" ]
	then
		echo OK
	else
		echo FAILED
		echo ""
		cat $tt.diffs
		echo ""
		echo "Try 'od -c' to compare the files"
	fi
done
