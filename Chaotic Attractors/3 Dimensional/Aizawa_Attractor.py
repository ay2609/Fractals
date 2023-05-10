import numpy as np
import matplotlib.pyplot as plt

def Aizawa(xyz, abcdef):
    x, y, z = xyz
    a, b, c, d, e, f = abcdef
    
    dx = (z-b) * x - d*y
    # print(dx)
    dy = d * x + (z-b) * y
    dz = c + (a*z) - ((z**3)/3) - ((x**2) + (y**2))*(1 + e*z) + (f*z*(x**3))
    return np.array([dx,dy,dz])
abcdef = (0.95,0.7,0.6,3.5,0.25,0.1)


dt = 0.01
steps = 250000

XYZ = np.empty((steps+1,3))
XYZ[0] = (0.1,0.,0.)

for i in range(steps):
    XYZ[i+1] = XYZ[i] + Aizawa(XYZ[i],abcdef) * dt
ax = plt.figure().add_subplot(projection='3d')

# print(xyzs.T)

ax.plot(*XYZ.T, '.',color='cyan',markersize=0.025)
ax.set_facecolor('black')
ax.axis('off')
ax.set_title("Aizawa Attractor")

plt.show()