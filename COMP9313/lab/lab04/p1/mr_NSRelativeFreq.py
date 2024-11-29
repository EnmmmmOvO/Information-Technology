### Note that if you use a single reducer, it is not necessary to configure JOBCONF.
### Since Hadoop automatically sorts the keys (a pair of terms) in alphabetical order.

import re
from mrjob.job import MRJob

class NSRelativeFreq(MRJob):                
   
    def mapper(self, _, line):
       words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())

       for i in range(0, len(words)):
           if len(words[i]):           
               for j in range(i+1, len(words)):
                   if len(words[j]):
                       yield words[i]+","+words[j], 1
                       yield words[i]+",*", 1
                       
    def combiner(self, key, values):
        yield key, sum(values)
            
    def reducer_init(self):
        self.marginal = 0
           
    def reducer(self, key, values):        
        wi, wj = key.split(",", 1)
        if wj=="*":
            self.marginal = sum(values)
        else:
            count = sum(values)
            yield key, count/self.marginal        
    
if __name__ == '__main__':
    NSRelativeFreq.run()
