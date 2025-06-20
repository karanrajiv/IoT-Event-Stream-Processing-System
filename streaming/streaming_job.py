
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType, LongType

spark = SparkSession.builder     .appName("IoTStreamProcessor")     .getOrCreate()

schema = StructType() \
    .add("sensor_id", StringType()) \
    .add("timestamp", DoubleType()) \
    .add("temperature", DoubleType()) \
    .add("humidity", DoubleType())

df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "sensor-data")     .load()

df_parsed = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

query = df_parsed.writeStream     .format("console")     .start()

query.awaitTermination()
