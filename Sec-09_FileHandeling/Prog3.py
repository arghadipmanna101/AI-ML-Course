import pandas as pd
from io import StringIO
url="https://www.fdic.gov/resources/resolutions/blank-failures/failed-bank-list/"
df=pd.read_html(url)
print(df)