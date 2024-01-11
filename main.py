from pyspark.sql import SparkSession
import config


def main():
    spark = SparkSession.builder.appName('DE_postings').getOrCreate()
    df = spark.read.csv(config.DATA_PATH, header=True)
    df.show(5)


if __name__ == '__main__':
    main()
