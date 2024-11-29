#!/usr/bin/python3

import re
import sys


for line in sys.stdin:
    line = line.strip()

    words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())

    for word in words:
        if len(word):
            print (word + "\t" + "1")

