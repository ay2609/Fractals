import numpy as np
import math
import gmpy2

sum = 0
exp = 1

for i in range(500):
    sum += (exp**i)/(math.factorial(i))
    print(sum)

print("Final Sum:",sum)
