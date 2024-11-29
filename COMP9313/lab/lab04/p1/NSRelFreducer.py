#!/usr/bin/python3
import sys
  
current_pair = None
current_sum = 0
current_count = 0
pair = None
  
# read the entire line from STDIN
for line in sys.stdin:
    line = line.strip()
    pair, count = line.split('\t', 1)

    count = int(count)
    
    if current_pair == pair:
        current_count += count
    else:        
        if current_pair:            
            wi, wj = current_pair.split(',', 1)
            if wj == "*":
                current_sum = current_count
            else:
                value = current_count/current_sum
                print(current_pair+"\t"+str(value))
        
        current_count = count
        current_pair = pair  

# Do not forget the last pair
wi, wj = current_pair.split(',', 1)
value = current_count/current_sum
print(current_pair+"\t"+str(value))
