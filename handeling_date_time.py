import pandas as pd
from datetime import datetime
df = pd.read_csv("customer_transaction_data.csv")
print(df.head())
print(df.columns)
x = df.loc[0,"order_date"]
print(x,type(x))

#Convert String to DateTime in Python
#y = "2021-05-17 23:47:50"
print(df['order_date'].dtype) #object

df['order_date'] = pd.to_datetime(df['order_date'])
print(df['order_date'].dtype) #datetime64[ns]