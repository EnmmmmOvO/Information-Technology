from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
import sys

class Problem3:

    def Question2(self, fields):
        puPairDF = fields.filter(col("VoteTypeId") == "5").select("PostId", "UserId").distinct().withColumn("PostId", col("PostId").cast("int")).withColumn("UserId", col("UserId").cast("int"))
        countsDF = puPairDF.groupBy("PostId").agg(collect_list("UserId").alias("userList"), count("PostId").alias("count")).filter(col("count") > 10)
        resDF = countsDF.select("PostId", "userList").withColumn("userList", sort_array(col("userList")))
        resDF.foreach(lambda x: print(str(x.PostId)+"#"+str(x.userList)))
    
    def Question1(self, fields):    	
        pvPairDF = fields.select("VoteTypeId", "PostId").distinct()
        countsDF = pvPairDF.groupBy("VoteTypeId").count().toDF("VoteTypeId", "numPosts").orderBy(-col("numPosts"))
        res = countsDF.take(5)
        for x in res:
            print(str(x.VoteTypeId) + "\t" + str(x.numPosts))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong inputs")
        sys.exit(-1)

    inputFile = sys.argv[1]
    spark = SparkSession.builder.master("local").appName("problem3").getOrCreate()
    fields = spark.read.csv(inputFile).toDF("Id", "PostId", "VoteTypeId", "UserId", "CreationTime")

    p3 = Problem3()
    p3.Question1(fields)
    p3.Question2(fields)
    spark.stop()
