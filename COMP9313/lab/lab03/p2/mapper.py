#!/usr/bin/python3

import re
import sys


for line in sys.stdin:
    line = line.strip()
    words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())

    for i in range(0, len(words)):
        if len(words[i]):
            tmp = {}
            for j in range(i + 1, len(words)):
                if len(words[j]):
                    tmp[words[j]] = tmp.get(words[j], 0) + 1
            
            print(words[i], tmp)

