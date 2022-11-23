import matplotlib.pyplot as plt
import numpy as np
#import symengine as sym
# def mapcolor(p: complex, count: int, accuracy: int) -> int:
size = 500
map = np.zeros((size, size), dtype=int)
thresh1 = 10
thresh2 = 10 #manipulate these 2 with c**x to get varying results

xdisp = 0
ydisp = 0
plane = 2.5
precision = 15

def iterate(x: complex, c: complex, count: int =0, accuracy=500) -> complex:
    # xn1 = c**x
    xn1 = x**2 + c
    map[np.absolute(xn1) > complex(thresh2,thresh2)] = count
    x[np.absolute(xn1) > complex(thresh1,thresh1)] = 0 + 0j
    # xn1[np.absolute(xn1) > complex(thresh1,thresh1)] = 0 + 0j
    c[np.absolute(xn1) > complex(thresh1,thresh1)] = 0 + 0j
    # print(xn1)
   # xn1 > 100+100j
 
    #check each iteration when a value has reached past a certain threshold, in which case you exempt it from continuing
    #iteration by setting its input and mandel array value back to 0 like in newtonraphson code,
    #assign it a value from counter to simulate shoot off speed
 
 
    # if np.absolute((xn1.real).all()) >= 10 or np.absolute(np.round((xn1.imag).all(),0)) >= 10j:
    #     return xn1
 
    if count == accuracy:
        return xn1
   
    return (iterate(xn1,inputs, count+1))
 
 
mandel = np.zeros((size,size), dtype = complex)

x = np.round(np.linspace(-(plane + xdisp), (plane + xdisp), size, dtype=complex), precision)
y = np.round(np.linspace(-(plane + ydisp)*1j,(plane + ydisp)*1j, size, dtype=complex), precision)

inputs = x + y[:, np.newaxis]
 
mandel = iterate(mandel,inputs)
 
i = 592
k = 716
# print(i, k, mandel[i][k])
 
 
 
# map[mandel<10] = 1
# map[map == 0] = 2
# map[map == 1] = 0
 
 
fig, ax = plt.subplots()
plt.imshow(map,cmap=plt.cm.magma)
# plt.imshow(map,cmap=plt.cm.YlOrRd)
# plt.matshow(map,cmap=plt.cm.Blues)
ax.invert_yaxis()
plt.axis('off')
plt.show()
 
 
 
 
###MAKE ANOTHER MATRIX FULL OF Y VALUES AND GRAPH THAT TOO, 3 D FUNCTIONS!!!!
### Graph Riemann Sum vector field
# https://www.youtube.com/watch?v=sD0NjbwqlYw
