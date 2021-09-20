## 2021-09-19 20:43:55

import pandas as pd
from pandas._libs.missing import NA

## Read csv
csv1 = pd.read_csv('../dataFile.csv')

## create dataframe
df1 = pd.DataFrame(csv1)

## [x] Print first 10 rows
print("first 10 rows")
print(df1.head(10))

print('-------------------------------------------')
## [x] print last 5 rows
print("last 5 rows")
print(df1.tail(5))

print('-------------------------------------------')

## [x] Create new dataframe by removing rows with empty cells (how many?)
df2 = pd.DataFrame(df1)

print("Create new dataframe by removing rows with empty cells (how many?)")
print(df2.dropna().count())

print('-------------------------------------------')

## [ ] create new dataframe by replacing empty values with '111'
df3 = pd.DataFrame(df1)

print('-------------------------------------------')

print(df3.fillna('111').loc[0:20])
print('-------------------------------------------')

## [x] print mean, median for Pulse column

print("mean, median - Pulse column")
print(df1['Pulse'].mean())
print(df1['Pulse'].median())


### [x] sort dataframe by column

df1last5sorted = df1.tail(5).sort_values(by='Duration', ascending=False)
print('-------------------------------------------')

print(df1last5sorted)
