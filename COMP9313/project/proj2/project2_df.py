from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import sys

class Project2:
    @staticmethod
    def run(inputPath, outputPath, stopwords, k):
        spark = SparkSession.builder.master("local").appName("project2_df").getOrCreate()

        # Reads the input file and extracts the year and word fields.
        df = spark.read.text(inputPath) \
            .withColumn("year", col("value").substr(1, 4)) \
            .withColumn("words", split(col("value"), ",", 2)[1])

        # Get the stopword list
        stopword = df.select(explode(split(col("words"), " ")).alias("word")) \
            .filter(length("word") > 0)  \
            .groupBy("word") \
            .count() \
            .orderBy(desc("count"), asc("word")) \
            .limit(int(stopwords)) \
            .collect()

        stopword = [row["word"] for row in stopword]

        # Calculate the term frequency (TF) of each word in each year.
        tf = df.select(col("year"), explode(split(col("words"), " ")).alias("word")) \
            .filter((length("word") > 0) & (~col("word").isin(stopword))) \
            .groupBy("year", "word") \
            .count() \
            .withColumnRenamed("count", "tf")

        # Calculate the total number of documents per year.
        year = df.select(col("year")).groupBy("year").count().withColumnRenamed("count", "year_count")

        # Calculate the IDF value of each word in each year. (Remove duplicate words in each line)
        idf = df.withColumn("unique_words", array_distinct(split(col("words"), " "))) \
            .select(col("year"), explode(col("unique_words")).alias("word")) \
            .filter((length("word") > 0) & (~col("word").isin(stopword))) \
            .groupBy("year", "word") \
            .count() \
            .withColumnRenamed("count", "idf")

        # Calculate TF-IDF and find the average weight of each word per year
        tf.join(idf, ["year", "word"], "inner") \
            .join(year, "year", "inner") \
            .withColumn("tf", log10(col("tf"))) \
            .withColumn("idf", log10(col("year_count") / col("idf"))) \
            .withColumn("tf_idf", col("tf") * col("idf")) \
            .groupBy("word") \
            .agg(avg("tf_idf").alias("avg_weight")) \
            .orderBy(desc("avg_weight"), asc("word")) \
            .limit(int(k)) \
            .withColumn("output", concat_ws("\t", "word", "avg_weight")) \
            .select("output") \
            .coalesce(1) \
            .write.text(outputPath)

        spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Wrong arguments")
        sys.exit(-1)
    Project2().run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
