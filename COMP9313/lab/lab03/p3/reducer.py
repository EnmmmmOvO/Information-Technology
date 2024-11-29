#!/usr/bin/python3
import sys

results = {}
for line in sys.stdin:
    word, frequency = line.strip().split('\t', 1)
    results[word] = results.get(word, 0) + int(frequency)
words = list(results.keys())

for word in words:
	w1, w2 = word.split(",",1)
	print(w1, w2, results[word])
