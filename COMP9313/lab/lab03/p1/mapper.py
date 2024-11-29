#!/usr/bin/python3

import re
import sys

# this is combiner
tmp = {}

for line in sys.stdin:
    line = line.strip()
    words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())

    for i in range(0, len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) and len(words[j]):
                k = words[i] + ";" + words[j]
                tmp[k] = tmp.get(k, 0) + 1

for k, v in tmp.items():
    print (k + '\t' + str(v))


