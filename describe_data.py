import pandas as pd

url = "https://raw.githubusercontent.com/isu-abe/516x/master/data/surveys1977.csv"
df = pd.read_csv(url, sep = ",", index_col=0)
print(df.describe())
