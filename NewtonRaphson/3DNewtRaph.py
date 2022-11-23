import matplotlib.pyplot as plt
import numpy as np
# import pygnuplot

size = 1000
precision = 20

r1, r2, r3 = 1-0j, np.round(-0.500000000000000 - 0.866025403784439j,2), np.round(-0.500000000000000 + 0.866025403784439j,2)
print(r2,r3)
map = np.zeros((size, size), dtype=int)
def iterate(x: complex, count: int =0, accuracy:int = 100) -> complex:
    xn1 = np.round((x - ((x**3-1)/(3*(x**2)))),precision)
    # xn1 = (x - (f(x))/(f2(x))).round(precision)
 
    # map[np.round(xn1,2)-r1==(0+0j)] = count
    # xn1[np.round(xn1,2)-r1==(0+0j)] = 0 + 0j
    # map[np.round(xn1,2)-r2==(0+0j)] = count + 1
    # xn1[np.round(xn1,2)-r2==(0+0j)] = 0 + 0j
    # map[np.round(xn1,2)-r3==(0+0j)] = count + 2
    # xn1[np.round(xn1,2)-r3==(0+0j)] = 0 + 0j
 
    if count == accuracy:
        return xn1
   
    return (iterate(xn1, count+1))
 
#can make it so that you check the map array for the highest value and it'll give you the most optimized accuracy,
#since after a certain point every value for your thing will have reached a root by some number


x = np.round(np.linspace(-.75, .75, size, dtype=complex), precision)
y = np.round(np.linspace(-.75j, .75j, size, dtype=complex), precision)
inputs = x + y[:, np.newaxis]
 
f = lambda x1: x1**3 - 1
f2 = lambda x1: 3*x1**2
#roots
r1, r2, r3 = 1-0j, -.5 - .87j, -.5+.87j
 
outputs = iterate(inputs, accuracy=50)
 
 
 
diff1 = r1 - outputs
diff2 = r2 - np.round(outputs,2)
diff3 = r3 - np.round(outputs,2)
# diff4 = r4 - outputs
 
map[diff1==(0+0j)] = 1
map[diff2==(0+0j)] = 2
map[diff3==(0+0j)] = 3
#map[diff3==(0+0j)] = 4
 
fig, ax = plt.subplots()

# plt.imshow(map)
plt.imshow(map,cmap= plt.cm.magma)
ax.invert_yaxis()
plt.axis('off')
plt.show()
 
 
 
##ROOT FINDER
 
 
###MAKE ANOTHER MATRIX FULL OF Y VALUES AND GRAPH THAT TOO, 3 D FUNCTIONS!!!!
### Graph Riemann Sum vector field
# https://www.youtube.com/watch?v=sD0NjbwqlYw
