from pyspark.sql import SparkSession
# Create Spark Session
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()
# load data
data = spark.read.csv("", header=True, inferSchema=True)
data.csv

# perform operations
result = data.groupBy("name ").agg({"score": "sum"})
# show result
result.show()
spark.stop
