import re
from mrjob.job import MRJob

class CoTermSynPair(MRJob):
    """
    You can also add a combiner. However, the combiner does not help much for this problem.   
    """

    def mapper(self, _, line):
        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        
        for index, w in enumerate(words):
            if len(w):
                for u in words[index+1:]:
                    if len(u):
                        w_, u_ = sorted([w, u])
                        k = "{} {}".format(w_, u_)
                        yield k, 1
    
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    CoTermSynPair.run()
