## matplotlib helpers

**matplotlib for ploting and visualization**

> Note: You can to use pandas and numpy with matplotlib

## first import matplotlib

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # +
```

## Simple matplotlib usage

```python
arr4 = np.arange(10)
plt.plot(arr4)
plt.show()

plt.plot(arr4, 'g--')
plt.show()

plt.plot(arr4, 'bo') #plot using blue circle markers

plt.plot(arr4, 'r+') #using red plus '+' sign

plt.plot(arr4, 'k*')


plt.title('Center Title')
plt.plot(arr4)
plt.title('Left Title', loc='left')
#plt.title('Right Title', loc='right')

# Figures and Subplots
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

'''
For more in matplotlib, Refer to:
 https://matplotlib.org/3.1.1/index.html
'''

```
