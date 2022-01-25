import findspark
import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

findspark.init()


spark = SparkSession.builder.config('spark.master','local').\
    config('spark.app.name','s3app').\
    getOrCreate()

print(spark)
sc = spark.sparkContext
print(sc)

hadoop_conf=sc._jsc.hadoopConfiguration()
access_id = ""
access_key = ""
hadoop_conf.set("fs.s3n.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
hadoop_conf.set("fs.s3n.awsAccessKeyId", access_id)
hadoop_conf.set("fs.s3n.awsSecretAccessKey", access_key)
df=spark.read.json("s3n://iris.json")
df.show()

