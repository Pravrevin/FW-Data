import boto3
import pandas as pd
from io import StringIO
from pyspark.sql import SparkSession
import findspark
from pyspark.sql.functions import isnan, when, count, col
from pyspark.sql.functions import *
from pyspark.sql.functions import col,isnan, when, count
findspark.init()
bucket_name = 'genome-landing-zone'
feed_name = 'customertxn'
app_name = 'tata-cliq'
date = '27-01-2022'
object_name = 'customer_transaction_data.csv'
object_key_final = app_name +'/'+ feed_name +'/'+ date +'/'+object_name

print(object_key_final)
s3_client_get = boto3.client(
            's3',
        aws_access_key_id='akhilAKIAX5VSTrumanI6XZPZSsanjay2JHL',
        aws_secret_access_key='akhiluv4FWPH9Frumanbz8ysanjayhj/EwiCDEGPaLw3fLbz8E4B7fuZ'
        )
csv_obj = s3_client_get.get_object(Bucket=bucket_name, Key=object_key_final)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))
column_name = list(df.columns)
print(column_name)

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("genome") \
    .getOrCreate()

sparkDF=spark.createDataFrame(df)
print(sparkDF.printSchema())

count_null_values = sparkDF.select([count(when(isnan(c), c)).alias(c) for c in sparkDF.columns]).show()
print(sparkDF.dtypes)

#null values filling
sparkDF.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in sparkDF.columns]
   ).show()
for var in sparkDF.columns:
    datatype = dict(sparkDF.dtypes)[var]
    #print(datatype)
    if datatype == 'bigint':
        sparkDF.fillna(0)
        print('Filling Null values for',var)
    if datatype == 'string':
        sparkDF.fillna("NA")
        print('Filling Null values for', var)

#removing leading trailing spaces
for var in sparkDF.columns:
    datatype = dict(sparkDF.dtypes)[var]
    if datatype == 'string':
        print('Removing Leading & trailing whitespaces for',var)
        sparkDF = sparkDF.withColumn(str(var), trim(col(str(var))))

#Drop Duplicates rows
count_of_rows = sparkDF.count()
distinctDF = sparkDF.distinct().count()
print("Distinct count: ",distinctDF)
print(count_of_rows)
if count_of_rows > distinctDF:
    print('Removing Duplicates Rows')
