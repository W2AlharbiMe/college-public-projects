# basics of pandas chapter 1
# 2021-09-12 08:28:57

import pandas as pd

print("Pandas Version: ", pd.__version__)


a = [1, 7, 3]


series = pd.Series(a, index=["X", "Y", "Z"])

print('--- Output ---')
print(series)
