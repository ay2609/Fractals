import numpy as np
import matplotlib.pyplot as plt
import math




# print(np.round(np.sin(2*math.pi),5))

ab = (6.942,0.69)

# ab = (4.0,0.9)
# ab = (3.0,0.9)

def MFoldHenon(xy, ab):
    x, y = xy
    a, b = ab
    
    dx = 1 - a*np.sin(x) + b*y
    dy = x
    # print(dy)
    return np.array([dx,dy])

dt = 1
steps = 250000

XY = np.empty((steps+1,2))
XY[0] = (0.5,0.3)

for i in range(steps):
    XY[i+1] = MFoldHenon(XY[i],ab) * dt


XY = XY.T

fig,ax = plt.subplots()

fig.set_facecolor("black")

ax.scatter(*XY, s=0.1,color="white",alpha=0.6,linewidths=0)
plt.axis('off')

plt.show()