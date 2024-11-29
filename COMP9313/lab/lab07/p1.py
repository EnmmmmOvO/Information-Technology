from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
import sys

class Problem1:
    def run(self, inputPath, outputPath):
        spark = SparkSession.builder.master("local").appName("problem1").getOrCreate()

        fileDF = spark.read.text(inputPath)
        wordsDF = fileDF.selectExpr("explode(split(value, ' ')) as word").withColumn("word", lower(col("word")))
        wordsDF = wordsDF.filter(length(col("word")) >=1).filter((col("word").substr(0,1)<= 'z') & (col("word").substr(0,1)>='a'))

        letterDF = wordsDF.withColumn("word", col("word").substr(0, 1)).toDF("letter")
        countsDF = letterDF.groupBy("letter").count().orderBy("letter")
        countsDF.write.format("csv").save(outputPath)
        spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong inputs")
        sys.exit(-1)
    Problem1().run(sys.argv[1], sys.argv[2])
