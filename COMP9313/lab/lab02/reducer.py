#!/usr/bin/python3

import sys

result = {}

for line in sys.stdin:
    word, freq = line.strip().split('\t', 1)
    result[word] = result.get(word, 0) + int(freq)

for k, v in result.items():
    print(k, v)