from pyspark.sql import SparkSession


def create_spark(app_name: str):

    spark = (
        SparkSession.builder
        .appName(app_name)
        .config("spark.sql.shuffle.partitions", "8")
        .getOrCreate()
    )

    return spark