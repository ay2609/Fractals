import numpy as np
import matplotlib.pyplot as plt
import math




# print(np.round(np.sin(2*math.pi),5))

ab = (0.7,-0.82)

def Cathala(xy, ab):
    x, y = xy
    a, b = ab
    
    dx = a*x + y
    dy = b + x**2
    # print(dy)
    return np.array([dx,dy])

dt = 1
steps = 250000

XY = np.empty((steps+1,2))
XY[0] = (0.5,0.3)

for i in range(steps):
    XY[i+1] = Cathala(XY[i],ab) * dt


XY = XY.T

fig,ax = plt.subplots()

fig.set_facecolor("black")

plt.plot(XY[0,:],XY[1,:],'.',color="white",alpha=0.2, markersize=0.1)
plt.axis('off')

plt.show()