import os
import time

from pyspark.sql.session import SparkSession
import pyspark.sql.functions as F
import sys
from itertools import combinations

from pyspark.sql.types import ArrayType, StringType


class Project3:
    @staticmethod
    def run(inputPath: str, outputPath: str, d: float, s: float):
        spark = SparkSession.builder.master("local").appName("project3").getOrCreate()

        df = (spark.sparkContext.textFile(inputPath) \
            .map(lambda line: line.split("#")) \
            .map(lambda m: (
            int(m[0]),
            float(m[1][1:-1].split(",")[0]),
            float(m[1][1:-1].split(",")[1]),
            m[2].split(" ")
        )).toDF(["id", "x", "y", "terms"])
              .withColumn("terms_size",  F.size(F.col("terms")))
              .withColumn("grid", F.struct(F.floor(F.col("x") / F.lit(d)), F.floor(F.col("y") / F.lit(d)))))

        def generate_combinations(prefix, min_length, max_length):
            result = []
            for r in range(int(min_length), int(max_length) + 1):
                result.extend(["_".join(map(str, comb)) for comb in combinations(prefix, r)])
            return result

        generate_combinations_udf = F.udf(
            lambda prefix, min_length, max_length: generate_combinations(prefix, min_length, max_length),
            ArrayType(StringType()))

        pair = df.withColumn("min_match", F.greatest(F.floor(F.col("terms_size") * F.lit(s)), F.lit(1))) \
            .withColumn("block_keys",
                        generate_combinations_udf(F.col("terms"), F.col("min_match"), F.col("terms_size"))) \
            .select("id", "grid", F.explode("block_keys").alias("block_key")) \
            .groupBy("block_key") \
            .agg(F.collect_list(F.struct("id", F.col("grid"))).alias("record_ids_with_grid")) \
            .filter(F.size(F.col("record_ids_with_grid")) >= 2) \
            .withColumn("record_exploded_1", F.explode(F.col("record_ids_with_grid"))) \
            .withColumn("record_exploded_2", F.explode(F.col("record_ids_with_grid"))) \
            .filter(
                (F.col("record_exploded_1.id") < F.col("record_exploded_2.id")) &
                (F.abs(F.col("record_exploded_1.grid.col1") - F.col("record_exploded_2.grid.col1")) <= 1) &
                (F.abs(F.col("record_exploded_1.grid.col2") - F.col("record_exploded_2.grid.col2")) <= 1)
            ) \
            .select(
                F.col("record_exploded_1.id").alias("record_id_1"),
                F.col("record_exploded_2.id").alias("record_id_2")
            )

        df1 = df.alias("df1")
        df2 = df.alias("df2")

        pair.join(df1, pair["record_id_1"] == F.col("df1.id"), "left") \
            .join(df2, pair["record_id_2"] == F.col("df2.id"), "left") \
            .withColumn(
                "similarity",
                F.size(F.array_intersect(F.col("df1.terms"), F.col("df2.terms"))) /
                F.size(F.array_union(F.col("df1.terms"), F.col("df2.terms")))
            ) \
            .filter(F.col("similarity") >= s) \
            .withColumn(
                "distance",
                F.sqrt(F.pow(F.col("df1.x") - F.col("df2.x"), 2) + F.pow(F.col("df1.y") - F.col("df2.y"), 2))) \
            .filter(F.col("distance") <= d) \
            .select("record_id_1", "record_id_2", "distance", "similarity") \
            .distinct() \
            .orderBy("record_id_1", "record_id_2") \
            .select(F.concat(
                F.lit("("),
                F.col("record_id_1"),
                F.lit(","),
                F.col("record_id_2"),
                F.lit("):"),
                F.round(F.col("distance"), 6).cast("string"),
                F.lit(", "),
                F.round(F.col("similarity"), 6).cast("string")
            ).alias("text")) \
            .coalesce(1) \
            .write.text(outputPath)

        spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: spark-submit project3.py <inputPath> <outputPath> <d> <s>")
        sys.exit(-1)

    Project3().run(
        inputPath=sys.argv[1],
        outputPath=sys.argv[2],
        d=float(sys.argv[3]),
        s=float(sys.argv[4])
    )
