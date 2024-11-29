import re
from mrjob.job import MRJob

class CoTermNSPair(MRJob):

    def mapper(self, _, line):
        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) and len(words[j]):
                    k = words[i] + " " + words[j]
                    yield k, 1
    
    def combiner(self, key, values):
        yield key, sum(values)
    
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    CoTermNSPair.run()
