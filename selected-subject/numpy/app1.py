import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.arange(10,51)
print("\n",data)

print("\n",data.mean())
print("\n",data.sum())
print("\n",data.min())
print("\n",data.max())
# plt.title('index one', loc='left')
# plt.title('index two', loc='right')
# plt.plot(data)
# plt.show()

a= np.ones((3,4))
print("\n",a)
print()
print("\n",a*4)

b = np.random.randint(1, 11, 12)

b=b.reshape(3,4)
print("\n", b)
print("\n",b.T)
print("--------------------------------------------")
df=pd.DataFrame(b, index=['index 1', 'index 2', 'index 3'], columns=['C1', 'C2', 'C3', 'C4'])
print("\n",df)

print('------------------------------------')

df[df < 5] = 99
print(df)
