import numpy as np
import matplotlib.pyplot as plt
import sympy
import time
import math
import random

# < 2 Hours/ 1-2

x = sympy.symbols('x')

solutions = sympy.solve(sympy.sin(x) ,x)

# for i in range(np.shape(solutions)[0]):
#     solutions[i] = sympy.simplify(solutions[i])
#     solutions[i] = complex(solutions[i].evalf())
# solutions = np.round(solutions,4)

start_time = time.time()

points = 1000

vals = np.zeros((1,points))
nong = np.linspace(1,5,points)


for j in range(points):
    
    n = nong[j]
    nold = 0
    for i in range(2000):
        nold = n
        n = n - (np.sin(n) - 1)/np.cos(n)
        if nold == n:
            print(i)
            vals[0,j] = np.round(n/(math.pi/2),0)
            break
        # print(n)
    vals[0,j] = np.round(n/(math.pi/2),0)

# tonnrfpmr
# make it so that it's colored based on distance from center, not actual final location.

vals = np.round(vals,0)

mapp = np.zeros((100,points))

for i in range(100):
    mapp[i,:] = vals

print("--- %s seconds ---" % (time.time() - start_time))

fig,ax = plt.subplots()
plt.imshow(mapp,cmap=plt.cm.gist_rainbow)
plt.show()

    

print(solutions)

