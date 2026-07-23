from pyspark.sql import SparkSession

def create_spark(app_name: str):

    spark = (
        SparkSession.builder
        .appName(app_name)
        .getOrCreate()
    )

    return spark