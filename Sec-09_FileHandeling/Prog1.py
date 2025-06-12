import pandas as pd
from io import StringIO
Data='{"employee_name":"James","email":"james@gmail.com","job_profile":[{"title1":"Team Lead","title2":"Sr.Developer"}]}'
df=pd.read_json(StringIO(Data))
print(df)
print(df.to_json())
print(df.to_json(orient='index'))
print(df.to_json(orient='records'))