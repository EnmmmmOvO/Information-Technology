### You need to configure JOBCONF if you use more than 1 reducer.
### In this specific task, you do not need to configure the comparator.
### However, if the second field of the key is an integer, like in Project 1, you have to configuer the comparator as well.

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
            
    SORT_VALUES = True
            
    JOBCONF = {
        'stream.num.map.output.key.fields':2,
        'mapreduce.map.output.key.field.separator':',',
        'mapreduce.job.reduces':2,
        'mapreduce.partition.keypartitioner.options':'-k1,1'
    }
    
if __name__ == '__main__':
    NSRelativeFreq.run()
