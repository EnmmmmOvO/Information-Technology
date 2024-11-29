from pyspark import SparkContext, SparkConf
import re
import sys

class Problem2:
    def run(self, inputPath, outputPath):
        conf = SparkConf().setAppName("problem2")
        sc = SparkContext(conf=conf)

        file = sc.textFile(inputPath)

        # split the sencence into words
        words = file.flatMap(lambda line: re.split("[\\s*$&#/\"'\\,.:;?!\\[\\](){}<>~\\-_]+", line))  
        # convert the words to lower case
        lowerWords = words.map(lambda x: x.lower())
        # valid the word length
        validWords = lowerWords.filter(lambda x: len(x) >= 1) 
        # filter by the first letter
        validWords = validWords.filter(lambda x: True if x[0] >= 'a' and x[0] <= 'z' else False)

        # Please note that the reduceByKey only accept (key,value) pairs which means that 
        # all the values should be contained in a tuple/list or arbitary datastructure that could be
        # regarded as a single element for the high order tuple.
        # For example (key,(v1,v2,v3)) is valid but (key,v1,v2,v3) is not since there are too many elements 
        # to unpack for spark.

        res = validWords.map(lambda x: (x[0], (1, len(x)))) 
        res = res.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

        res = res.map(lambda x: (x[0], x[1][1] / x[1][0]))

        # You can also use join method to concat the tuple by a comma
        res = res.sortByKey().map(lambda x: str(x[0]) + "," + str(x[1]))
        res.saveAsTextFile(outputPath)
        sc.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong inputs")
        sys.exit(-1)
    Problem2().run(sys.argv[1], sys.argv[2])
