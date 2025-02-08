import numpy as np
import matplotlib.pyplot as plt
import math

# Peter De Jong Attractor

# Z IS NOT REQUIRED

# print(np.round(np.sin(2*math.pi),5))


# abcd = (-0.759,2.449,1.253,1.5)
abcd = (-0.709, 1.638, 0.452, 1.74)


def Clifford(xy, abcd):
    x, y = xy
    a, b, c, d = abcd

    dx = np.sin(a * y) - np.cos(b * x)
    dy = np.sin(c * x) - np.cos(d * y)
    # dz = np.sin(x)# not required
    # print(dy)
    return np.array([dx, dy])


dt = 1
steps = 50000

XY = np.empty((steps + 1, 2))
XY[0] = (0.0, 0.)

for i in range(steps):
    XY[i + 1] = Clifford(XY[i], abcd) * dt

XY = XY.T

fig, ax = plt.subplots()

fig.set_facecolor("black")

plt.plot(XY[1, :], XY[0, :], '.', color="white", alpha=0.2, markersize=0.2)
plt.axis('off')

plt.show()
