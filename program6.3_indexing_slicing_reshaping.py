import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Indexing
print("Element:", arr[1][2])

# Slicing
print("Slice:\n", arr[0:2, 1:3])

# Reshaping
new_arr = arr.reshape(1, 9)
print("Reshaped:", new_arr)
