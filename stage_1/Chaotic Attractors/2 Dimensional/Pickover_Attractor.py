import numpy as np
import matplotlib.pyplot as plt
import math


#also known as the Clifford Attractor

# print(np.round(np.sin(2*math.pi),5))

# abcd = (-2, 1.6, 1.0, 0.7)
# abcd = (2.1, 1.7, -0.5, -1)
abcd = (-1.4, 1.7, 1.0, 0.7)
# abcd = (2, 1, -0.5, -1.01) # with dt 1.25 makes it go from 1D --> 2D
# abcd = (-1.8, -2.0, -0.5, -0.9)
# abcd = (1.6, -0.6, -1.2, 1.6)
# abcd = (-1.7, 1.8, -1.9, -0.4)


def clifford(xy, abcd):
    x, y = xy
    a, b, c, d = abcd

    dx = (np.sin(a*y) + c*np.cos(a*x)) * dt
    dy = (np.sin(b*x) + d*np.cos(b*y)) * dt
    # print(dy)
    return np.array([dx, dy])


dt = 1.35
steps = 150000

XY = np.empty((steps+1, 2))
XY[0] = (10.75, 8.2)

for i in range(steps):
    XY[i+1] = XY[i] + clifford(XY[i], abcd)

print(XY)

XY = XY.T

fig,ax = plt.subplots()

fig.set_facecolor("black")

plt.scatter(XY[0, :], XY[1, :], color="white", alpha=0.6, s=0.05, lw=0)
plt.axis('off')

plt.show()
