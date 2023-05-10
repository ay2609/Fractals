import numpy as np
import matplotlib.pyplot as plt
import math


#also known as the Clifford Attractor

# print(np.round(np.sin(2*math.pi),5))

# abcd = (-2, 1.6, 1.0, 0.7)
# abcd = (2.1, 1.7, -0.5, -1)
abcd = (-1.4, 1.6, 1.0, 0.7)
# abcd = (2, 1, -0.5, -1.01) # with dt 1.25 makes it go from 1D --> 2D
# abcd = (-1.8, -2.0, -0.5, -0.9)
# abcd = (1.6, -0.6, -1.2, 1.6)
# abcd = (-1.7, 1.8, -1.9, -0.4)

def Clifford(xy, abcd):
    x, y = xy
    a, b, c, d = abcd

    dx = np.sin(a*y) + c*np.cos(a*x)
    dy = np.sin(b*x) + d*np.cos(b*y)
    # print(dy)
    return np.array([dx,dy])

dt = 1
steps = 150000

XY = np.empty((steps+1,2))
XY[0] = (0.0,-0.0)

for i in range(steps):
    XY[i+1] = Clifford(XY[i],abcd) * dt


XY = XY.T

fig,ax = plt.subplots()

fig.set_facecolor("black")

plt.plot(XY[0,:],XY[1,:],'.',color="white",alpha=0.6, markersize=0.2)
plt.axis('off')
