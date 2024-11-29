import heapq
import math
import sys

from mrjob.compat import jobconf_from_env
from mrjob.job import MRJob
from mrjob.step import MRStep


class Pair:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    def __lt__(self, other):
        if self.count != other.count:
            return self.count <= other.count
        else:
            return self.word > other.word


class proj1(MRJob):
    def __init__(self, args=None):
        super().__init__(args)
        self.year = None
        self.appear = None
        self.cur = None
        self.count = None
        self.total = None
        self.list = None
        self.k = None

    def mapper(self, _, line):
        record = {}

        date, words = line.strip().split(',', 1)
        year = date[0:4]
        date = date[4:8]

        for i in words.split(' '):
            if len(i):
                record[i] = record.get(i, 0) + 1

        for word, times in record.items():
            yield f"a,{year},{word}, ", times
            yield f"a,{year},{word},{date}", 1

        yield f"a,{year}, , ", 1

    def reducer_init(self):
        self.year = ""
        self.count = 0
        self.cur = ""
        self.total = 0
        self.appear = 0
        self.list = []
        self.k = int(jobconf_from_env('myjob.settings.k'))
        heapq.heapify(self.list)

    def reducer(self, key, values):
        a, year, word, date = key.split(",")

        if year != self.year and year != "":
            for i in heapq.nlargest(len(self.list), self.list):
                yield self.year, f"{i.word},{i.count}"

            self.year = ""
            self.count = 0
            self.cur = ""
            self.total = 0
            self.appear = 0
            self.list = []


        if word == " ":
            self.total += sum(values)
        elif date == ' ':
            if self.cur != word:
                if self.cur != " ":
                    heapq.heappush(self.list, Pair(word=self.cur, count=self.count * math.log10(self.total/self.appear)))

                    if len(self.list) > self.k:
                        heapq.heappop(self.list)
                self.appear = 0
                self.count = 0
            self.count += sum(values)
        else:
            self.appear += sum(values)
        self.cur = word
        self.year = year

    def reducer_final(self):
        heapq.heappush(self.list, Pair(word=self.cur, count=self.count * math.log10(self.total/self.appear)))

        if len(self.list) > self.k:
            heapq.heappop(self.list)

        for i in heapq.nlargest(len(self.list), self.list):
            yield self.year, f"{i.word},{i.count}"

    SORT_VALUES = True

    def steps(self):
        JOBCONF = {
            'stream.num.map.output.key.fields': 4,
            'mapreduce.map.output.key.field.separator': ',',
            'mapreduce.partition.keypartitioner.options': '-k1,2',
            'mapreduce.job.output.key.comparator.class': 'org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator',
            'mapreduce.partition.keycomparator.options': '-k2,2n -k3,3 -k4,4'
        }

        return [MRStep(jobconf=JOBCONF, mapper=self.mapper, reducer=self.reducer, reducer_init=self.reducer_init,
                       reducer_final=self.reducer_final)]


if __name__ == '__main__':
    proj1.run()