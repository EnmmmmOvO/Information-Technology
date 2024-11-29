from mrjob.job import MRJob

class Job(MRJob):
    def mapper(self, key, value):
        for word in value.strip().split():
            if word[0].isalpha():
                yield word[0].lower(), 1

    def combiner(self, key, values):
        yield key, sum(values)
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    Job.run()