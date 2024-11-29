from pyspark import SparkContext, SparkConf
import sys
import math


def tf_count(line):
    # Split each line into date and words to calculate the term frequency (TF) of each word in each year.
    date, words = line.strip().split(',', 1)
    for  word in words.split():
        if len(word):
            yield (date[0:4], word), 1

def year_count(line):
    # Split each line into date and words to calculate the total number of documents per year.
    if len(line):
        return line[0:4], 1

def idf_count(line, stopword):
    # Split each line into date and words to calculate the IDF value of each word.
    date, words = line.strip().split(',', 1)

    # Remove duplicate words in each line
    for word in set(words.split()):
        if len(word) and  word not in stopword:
            yield (date[0:4], word), 1

def word_count(line):
    # Split each line into date and words to get the stopword list.
    _, words = line.strip().split(',', 1)

    for word in words.split():
        if len(word):
            yield word, 1

def calculator(x, y, data, year):
    # Calculate the TF-IDF and find the average weight of each word per year.
    tf = math.log10(data[(x[0], x[1])])
    idf = math.log10(year[x[0]] / y)
    return x[1], (tf * idf, 1)

class Project2:
    @staticmethod
    def run(inputPath, outputPath, stopwords, k):
        conf = SparkConf().setAppName("project2_rdd").setMaster("local")
        sc = SparkContext(conf=conf)

        # Load input data
        content = sc.textFile(inputPath)

        # Generate the stopword list by global word count
        stopword = content.flatMap(lambda x: word_count(x)) \
            .reduceByKey(lambda x, y: x + y) \
            .sortBy(lambda x: (-x[1], x[0])) \
            .map(lambda x: x[0]) \
            .take(int(stopwords)) \

        # Calculate term frequency (TF) for each word in each year
        data = content.flatMap(lambda line: tf_count(line)) \
            .reduceByKey(lambda x, y: x + y) \
            .collectAsMap()

        # Count the number of documents per year
        year = content.map(lambda line: year_count(line)) \
            .reduceByKey(lambda x, y: x + y) \
            .collectAsMap()

        # Calculate TF-IDF for each word in each year
        result = content.flatMap(lambda line: idf_count(line, stopword)) \
            .reduceByKey(lambda x, y: x + y) \
            .map(lambda x: calculator(x[0], x[1], data, year)) \
            .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \
            .map(lambda x: (x[0], (x[1][0] / x[1][1]))) \
            .coalesce(1) \
            .sortBy(lambda x: (-x[1], x[0])) \
            .coalesce(1) \
            .take(int(k))

        # Save the result as a text file
        sc.parallelize(result).map(lambda x: f"{x[0]}\t{x[1]}").saveAsTextFile(outputPath)

        sc.stop()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Wrong arguments")
        sys.exit(-1)
    Project2().run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
