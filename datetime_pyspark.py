from pyspark.sql.functions import unix_timestamp, from_unixtime
import pyspark
import findspark
from pyspark.sql import SparkSession
findspark.init()
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

df = spark.createDataFrame(
    [("11/25/1991",), ("11/24/1991",), ("11/30/1991",)],
    ['date_str']
)
print(df.show())
df2 = df.select(
    'date_str',
    from_unixtime(unix_timestamp('date_str', 'MM/dd/yyy')).alias('date')
)
print(df2.show())