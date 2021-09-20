#### Pandas helpers

#### Read csv file

```python
import pandas as pd
data = pd.read_csv('path/to/datafile.csv')
```

#### Create dataframe

```python
df = pd.DataFrame(data)
```

#### get first 10 rows

```python
df.head(10)
```

#### get last 5 rows

```python
df.tail(5)
```

#### remove rows with empty cells

```python
df.dropna() # use count() to get the number of how many deleted rows
```

#### replace empty values

```python
df.fillna('example')
```

#### find mean, median for a specific column

```python
# Mean
df['Pulse'].mean()
# Median
df['Pulse'].median()
```

#### Sort example

```python
# get last 5 rows and sort them in descending order by column `Duration`
df.tail(5).sort_values(by='Duration', ascending=False)
```
