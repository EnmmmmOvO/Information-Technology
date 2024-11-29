from pyspark import SparkContext, SparkConf
from operator import add
import sys

class Problem1:
    def run(self, inputPath, outputPath):
        conf = SparkConf().setAppName("problem1")
        sc = SparkContext(conf=conf)

        fp = sc.textFile(inputPath)

        words = fp.flatMap(lambda line: line.split(" "))  # split the sencence into words
        lowerWords = words.map(lambda x: x.lower())  # convert the words to lower case
        validWords = lowerWords.filter(lambda x: len(x) >= 1)  # valid the word length
        validWords = validWords.filter(lambda x: True if x[0] >= 'a' and x[0] <= 'z' else False)  # filter by the first letter

        res = validWords.map(lambda x: (x[0], 1))
        res = res.reduceByKey(add).sortByKey()  # add is a built-in method provided by pySpark

        res.saveAsTextFile(outputPath)
        sc.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong inputs")
        sys.exit(-1)
    Problem1().run(sys.argv[1], sys.argv[2])
