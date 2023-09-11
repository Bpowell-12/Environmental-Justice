import pandas as pd

df = pd.read_csv('Louisiana_county.csv', usecols = ('COUNTY', 'lOCATION'))

print(df.to_string())








