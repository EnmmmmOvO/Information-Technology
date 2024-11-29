#!/usr/bin/python3

import re
import sys


for line in sys.stdin:
    line = line.strip()
    words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())

    for index, w in enumerate(words):
        if len(w):
            tmp = {}
            for u in words[index+1:]:
                if len(u):
                    if w < u:
                        tmp[u] = tmp.get(u, 0) + 1
                    else:
                        print ("{}\t".format(u) + str({w : 1}))
            print (w + "\t" + str(tmp))
