import re
from mrjob.job import MRJob

class CoTermSynStripe(MRJob):
    """
    This version utlizes the in-mapper combining approach.
    However, for the stripes method, it would be better to use a combiner to avoid the memory issue.
    """

    def mapper_init(self):
        self.tmp = {}

    def mapper(self, _, line):
        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        
        for index, w in enumerate(words):
            if len(w):
                freq = {}
                for u in words[index+1:]:
                    if len(u):
                        if w < u:
                            freq[u] = freq.get(u, 0) + 1
                        else:
                            yield "{}".format(u), str({w : 1})
                
                if w in self.tmp:
                    for k, v in freq.items():
                        self.tmp[w][k] = self.tmp[w].get(k, 0) + int(v)
                else:
                    self.tmp[w] = freq

    def mapper_final(self):
        for k, v in self.tmp.items():
            yield k, str(v)
    
    def reducer(self, key, values):
        tmp_freq = {}
        for value in values:
            value = eval(value)
            for k, v in value.items():    
                tmp_freq[k] = tmp_freq.get(k, 0) + int(v)
        
        for kk, vv in tmp_freq.items():
            yield key + " " + str(kk), str(vv)

if __name__ == '__main__':
    CoTermSynStripe.run()
