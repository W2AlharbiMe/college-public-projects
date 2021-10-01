import pandas as pd


data = pd.read_csv('./dataFile.csv')


df = pd.DataFrame(data)


print('--- Get First 10 rows ---')
print(df.head(10))

print('--- Get Last 5 rows ---')
print(df.tail(5))


print('--- Get single row ---')
print(df.loc[17])


print('--- replace empty values ---')
newDf = df.fillna('111')
print(newDf.loc[17])


print('--- find mean, median for Pulse column ---')
print('Mean:', newDf['Pulse'].mean())
print('Median:', newDf['Pulse'].median())

# print('--- sort by Duration ascending ---')
# print(newDf.sort_values(by='Duration'))

# print('--- sort by Duration descending ---')
# print(newDf.sort_values(by='Duration', ascending=False))


print('--- display information about the data ---')
print(newDf.info())


print('--- print between indexes 0 to 20 ---')
print(newDf[0:20])


print('--- access a specific cell ---')
print(newDf.at[1, 'Duration'])
print(newDf.iat[1, 2])


print('--- calculate each values in column ---')
i = newDf['Duration'].value_counts()
print(i)


print('--- find the data correlations ---')
print(newDf.corr())

