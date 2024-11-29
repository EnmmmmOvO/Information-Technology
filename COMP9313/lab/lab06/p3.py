from pyspark import SparkContext, SparkConf
import sys

Id = 0
PostId = 1
VoteTypeID = 2
UserId = 3
CreationDate = 4
    
class Problem3:
    
    def Question1(self, fields):
        pairs = fields.map(lambda x: (x[VoteTypeID], set([x[PostId]])))

        res = pairs.reduceByKey(lambda x, y: x | y)
        res = res.map(lambda x: (x[0], len(x[1]))).sortByKey().sortBy(lambda x: x[1], ascending =False)
        res.foreach(lambda x: print(x))

    
    def Question2(self, fields):
        pairs = fields.map(lambda x: (x[PostId], set([x[UserId]])))
        # pairs = pairs.map(lambda x: x if None not in x[1] else (x[0], x[1].remove(None)))
        pairs = pairs.map(lambda x: x if "" not in x[1] else (x[0], x[1].remove("")))
        pairs = pairs.filter(lambda x: True if x[1] else False)
        res = pairs.reduceByKey(lambda x, y: x | y)

        res = res.filter(lambda x: True if len(x[1]) > 10 else False)
        res = res.map(lambda x: (x[0], sorted([int(item) for item in list(x[1])])))
        res = res.sortByKey()
        res = res.map(lambda x: f"{x[0]}#{','.join([str(item) for item in x[1]])}")
        
        res.foreach(lambda x: print(x))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong inputs")
        sys.exit(-1)
    conf = SparkConf().setAppName("problem3").setMaster("local")
    sc = SparkContext(conf=conf)
    
    textFile = sc.textFile(sys.argv[1])
    fields = textFile.map(lambda line: line.split(","))
    p3 = Problem3()
    p3.Question1(fields)
    p3.Question2(fields)
    sc.stop()
