#!/usr/bin/python3

import re
import sys


for line in sys.stdin:
    line = line.strip()
    words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())

    for index, w in enumerate(words):
        if len(w):
            for u in words[index+1:]:
                if len(u):
                    if w < u:
                        print("{},{}\t 1".format(w, u))
                    else:
                        print("{},{}\t 1".format(u, w))
