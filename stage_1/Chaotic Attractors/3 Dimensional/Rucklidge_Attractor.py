import numpy as np
import matplotlib.pyplot as plt

def Rucklidge(xyz, ka):
    x, y, z = xyz
    k,a = ka
    
    dx = -k*x + a*y - y*z
    dy = x
    dz = -z + y**2
    return np.array([dx,dy,dz])
ka = (2,6.7)


dt = 0.0075
steps = 250000

XYZ = np.empty((steps+1,3))
XYZ[0] = (1,0.,0.)

for i in range(steps):
    XYZ[i+1] = XYZ[i] + Rucklidge(XYZ[i],ka) * dt
ax = plt.figure().add_subplot(projection='3d')

# print(xyzs.T)

ax.plot(*XYZ.T,color='blue',lw=0.05)
# ax.set_facecolor('black')
# ax.axis('off')
ax.set_title("Rucklidge Attractor")

plt.show()