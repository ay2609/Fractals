import numpy as np
import math

arr1 = np.arange(0,10,1)
arr2 = np.zeros(len(arr1))
# print("arr1", len(arr1))
# print("arr2", len(arr2)
arr3 = np.vstack((arr1,arr2))
print(arr3[0])
