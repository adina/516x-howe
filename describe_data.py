import pandas as pd
import sys

file_to_open = open(sys.argv[1], 'r')
#url = "https://raw.githubusercontent.com/isu-abe/516x/master/data/surveys1977.csv"
df = pd.read_csv(file_to_open, sep = ",", index_col=0)
print(df.describe())
