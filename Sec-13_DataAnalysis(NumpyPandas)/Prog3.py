import pandas as pd
df1=pd.DataFrame({'key':['A','B','C'],'value1':[1,2,3]})
df2=pd.DataFrame({'key':['A','B','D'],'value2':[4,5,6]})
print(df1)
print(df2)
print(pd.merge(df1,df2,on="key",how="inner"))
print(pd.merge(df1,df2,on="key",how="outer"))
print(pd.merge(df1,df2,on="key",how="left"))
print(pd.merge(df1,df2,on="key",how="right"))