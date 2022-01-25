import boto3
import pandas as pd
from io import StringIO


bucket_name = 'genome-landing-zone'
object_key = 'customer_transaction_data.csv'

s3_resource = boto3.client(
            's3',
            aws_access_key_id='',
            aws_secret_access_key=''
        )

csv_obj = s3_resource.get_object(Bucket=bucket_name, Key=object_key)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))
column_name = list(df.columns)

#Replacing Null Values
for var in column_name:
    df[var].fillna("NA", inplace=True)
print('Replacing Null Values Done')

#removing trailing & leading spaces
for var in column_name:
    if df[var].dtypes == "object":
        df[var].str.strip()
print('Removing Trailing & leading spaces done')

#Removing duplicates values
#sort-PK
df.drop_duplicates(keep=False,inplace=True)
print('Remove Duplicates value done')

print (df.head())