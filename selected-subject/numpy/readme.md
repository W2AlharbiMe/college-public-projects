#### Numpy helpers

## First Import Numpy!

```python
import numpy as np
```

## Generate Random Numbers

```python
np.random.randn(2, 3)
```

## Return evenly spaced values within a given interval

```python
np.arange(10)
```

## Creating and converting to ndarrays

```python
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
```

## Get Array Dimensions Number

```python
print(arr1.ndim)
```

## Create a matrix from zeros

```python
zero_matrix = np.zeros((3, 6))
```

## Create a matrix from number 1

```python
ones_matrix = np.ones((4,5))
```

## Indexing and Slicing

```python
eight_m = ones_matrix * 8
print(eight_m)

# Print from index 5 to index 8
print(arr[5:8])

# Update values within a range
arr[2:5] = 12

# Change all items in array
arr[0:] = 5
arr[:] = 9

# 3-D slicing
arr3d = np.arange(12)
print(arr3d)
arr3d = arr3d.reshape(2,2,3)
print(arr3d)
```

## linear Algebra

```python
x = np.random.randint(0, 9, 20)
x = x.reshape(4,5)

# Transpose
x.T

#dot product
dot = np.dot(x, x.T)

# Square Root
np.sqrt(m)

# Sum
print(x.sum())
print(x[1, 0:].sum()) # sum 1st row only
print(x[:, 3].sum()) # sum of 3rd column
print(x[3, :].sum()) # sum of 4th row
print(x[3].sum()) ## sum of 4th row
print(x.sum(axis = 0))
print(x.sum(axis = 1))

# Get mean
x.mean()
x[1,:].mean()
```
