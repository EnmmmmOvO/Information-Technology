#!/usr/bin/python3

import sys
import re

for line in sys.stdin: 
   line = line.strip() 
   words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        
   for i in range(0, len(words)):
       if len(words[i]):           
           for j in range(i+1, len(words)):
               if len(words[j]):
                   print (words[i]+","+words[j]+"\t1")
                   print (words[i]+",*\t1")
