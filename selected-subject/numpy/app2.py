import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = np.random.randint(10, 51, size=10)

print('Sum:',data.sum())
print('Mean:',data.mean())
print('Min:',data.min())
print('Max:',data.max())
print(data)

# Q 3
# plt.plot(data)
# plt.show()
print('--------------------------')

a = np.ones((3, 4))
print(a*4)


print('--------------------------')

b = np.random.randint(1, 11, size=(3, 4))
print(b.T)

print('--------------------------')


df = pd.DataFrame(b, index=['index 1', 'index 2', 'index 3'], columns=['Column 1', 'Column 2', 'Column 3', 'Column 4'])
print(df)

print('--------------------------')

df[df < 5] = 99
print(df)
