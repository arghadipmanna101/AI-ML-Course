import pandas as pd
from io import StringIO
df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",header=None)
print(df.head())
df.to_csv("Data.csv")
