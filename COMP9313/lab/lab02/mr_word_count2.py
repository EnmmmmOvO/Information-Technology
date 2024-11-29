import re
from mrjob.job import MRJob

class WordCount(MRJob):

    def mapper_init(self):
        self.tmp = {}

    def mapper(self, _, line):
        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", line.lower())
        for word in words:
            if len(word):
                self.tmp[word] = self.tmp.get(word, 0) + 1
    
    def mapper_final(self):
        for k, v in self.tmp.items():
            yield (k, v)

    
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    WordCount.run()
