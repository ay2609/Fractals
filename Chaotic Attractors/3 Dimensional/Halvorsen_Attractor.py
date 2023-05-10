import numpy as np
import matplotlib.pyplot as plt

def Halvorsen(xyz, a):
    x, y, z = xyz
    
    dx = -a*x - 4*y - 4*z - y**2
    # print(dx)
    dy = -a*y - 4*z - 4*x - z**2
    dz = -a*z - 4*x - 4*y - x**2
    return np.array([dx,dy,dz])
a = 1.89
dt = 0.01
steps = 250000

XYZ = np.empty((steps+1,3))
XYZ[0] = (1.,0.,0.)

for i in range(steps):
    XYZ[i+1] = XYZ[i] + Halvorsen(XYZ[i],a) * dt

ax = plt.figure().add_subplot(projection='3d')

# print(xyzs.T)

ax.plot(*XYZ.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Halvorsen Attractor")

plt.show()