import re
from mrjob.job import MRJob

class CoTermNSStripe(MRJob):
    """
    For combiner there are two versions,
    you can use combiner or in-mapper combiner
    """

    def mapper_init(self):
        self.tmp = {}

    def mapper(self, _, line):
        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        
        for i in range(0, len(words)):
            if len(words[i]):
                freq = {}
                for j in range(i + 1, len(words)):
                    if len(words[j]):
                        freq[words[j]] = freq.get(words[j], 0) + 1
                
                # merge the information
                if words[i] in self.tmp:
                    for k, v in freq.items():
                        self.tmp[words[i]][k] = self.tmp[words[i]].get(k, 0) + int(v)
                else:
                    self.tmp[words[i]] = freq
                
    
    def mapper_final(self):
        for k, v in self.tmp.items():
            yield k, str(v)

    # def mapper(self, _, line):
    #     words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        
    #     for i in range(0, len(words)):
    #         if len(words[i]):
    #             freq = {}
    #             for j in range(i + 1, len(words)):
    #                 if len(words[j]):
    #                     freq[words[j]] = freq.get(words[j], 0) + 1
                
    #             yield words[i], str(freq)
    
    
    # def combiner(self, key, values):
    #     tmp_freq = {}
    #     for value in values:
    #         value = eval(value)
    #         for k, v in value.items():
    #             tmp_freq[k] = tmp_freq.get(k, 0) + int(v)
        
    #     yield key, str(tmp_freq)
    
    def reducer(self, key, values):
        tmp_freq = {}
        for value in values:
            value = eval(value)
            for k, v in value.items():    
                tmp_freq[k] = tmp_freq.get(k, 0) + int(v)
        
        for kk, vv in tmp_freq.items():
            yield key + " " + str(kk), str(vv)

if __name__ == '__main__':
    CoTermNSStripe.run()
