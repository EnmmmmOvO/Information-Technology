#!/usr/bin/python3

import sys

result = {}

for line in sys.stdin:
    word, freq = line.strip().split(' ', 1)
    freq = eval(freq)

    if word in result:
        tmp_freq = result[word]
        for k, v in freq.items():
            tmp_freq[k] = tmp_freq.get(k, 0) + v
        result[word] = tmp_freq
    else:
        result[word] = freq

for k, v in result.items():
    if not len(v):
        continue

    for kk, kv in v.items():
        res = str(k)
        res += " " + str(kk) + " " + str(kv)
        print(res)