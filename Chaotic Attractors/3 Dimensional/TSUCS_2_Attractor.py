import numpy as np
import matplotlib.pyplot as plt



def TSUCS2(xyz, abcdef):
    x, y, z = xyz
    a,b,c,d,e,f = abcdef

    dx = a*(y-x) + d*x*z  
    dy = f*y + b*x - x*z
    dz = c*z + x*y  - e*(x**2)
    return np.array([dx,dy,dz])
abcdef = (40,55,1.833,0.16,0.65,20)


dt = 0.00001
steps = 1000000

XYZ = np.empty((steps+1,3))
XYZ[0] = (0.1,1.0,-0.1)

for i in range(steps):
    XYZ[i+1] = XYZ[i] + TSUCS2(XYZ[i],abcdef) * dt
ax = plt.figure().add_subplot(projection='3d')

# print(xyzs.T)

ax.plot(*XYZ.T,color='blue',lw=0.5)
# ax.set_facecolor('black')
# ax.axis('off')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("TSUCS2 Attractor")

plt.show()