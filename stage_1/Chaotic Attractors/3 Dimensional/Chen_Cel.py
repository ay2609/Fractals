#Chen Celilovsky attractor

import numpy as np
import matplotlib.pyplot as plt

def ChenCel(xyz, abc):
    x, y, z = xyz
    a, b, c = abc
    
    dx = a*(y - x)
    dy = c*y - x*z
    dz = x*y - b*z
    return np.array([dx,dy,dz])


abc = (36,3,20)


dt = 0.01
steps = 10000


XYZ = np.empty((steps+1,3))
XYZ[0] = (1.,2.,3.)

for i in range(steps):
    XYZ[i+1] = XYZ[i] + ChenCel(XYZ[i],abc) * dt

ax = plt.figure().add_subplot(projection='3d')

# print(xyzs.T)

ax.plot(*XYZ.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Chen Celilovsky Attractor")

plt.show()
