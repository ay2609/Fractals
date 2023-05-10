import numpy as np
import matplotlib.pyplot as plt

def SprottLinzF(xyz, a):
    x, y, z = xyz
    
    dx = y+z
    dy = -x + a*y
    dz = x**2 - z
    return np.array([dx,dy,dz])
a = 0.5


dt = 0.01
steps = 250000

XYZ = np.empty((steps+1,3))
XYZ[0] = (0.1,0.,0.)

for i in range(steps):
    XYZ[i+1] = XYZ[i] + SprottLinzF(XYZ[i],a) * dt
ax = plt.figure().add_subplot(projection='3d')

# print(xyzs.T)

ax.plot(*XYZ.T,color='blue',lw=0.05)
# ax.set_facecolor('black')
# ax.axis('off')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Sprott-Linz F Attractor")

plt.show()