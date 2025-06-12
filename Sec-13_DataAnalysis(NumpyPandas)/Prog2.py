import pandas as pd
df=pd.read_csv("Data.csv")
df=df.rename(columns={'Price','Car_Price'})
print(df.head())