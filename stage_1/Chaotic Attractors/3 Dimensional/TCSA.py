## Thomas’ Cyclically Symmetric Attractor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def Thomas(xyz, b, i):
    x, y, z = xyz
    
    dx = np.sin(y) - b*x
    dy = np.sin(z) - b*y
    dz = np.sin(x) - b*z

    XYZvelo[i] = np.sqrt((dx**2) + (dy**2) + (dz**2))


    return np.array([dx,dy,dz])
# b = 1
b = 0.208186
# b= 0.1998
# b = 0.32899
dt = 0.01
steps = 35000

# coloring = plt.cm.jet([0,steps])
# print(coloring)
XYZvelo = np.empty((steps+1))

XYZ = np.empty((steps+1,3))
XYZ[0] = (-0.33,-0.1,-0.25)
# XYZ[0] = (0.33,0.1,0.25)
for i in range(steps):
    XYZ[i+1] = XYZ[i] + Thomas(XYZ[i],b, i) * dt

XYZvelo = XYZvelo/max(XYZvelo)
XYZvelo = np.round(XYZvelo,3)


# XYZ2 = np.empty((steps+1,3))

# XYZ2[0] = (0.33,0.1,0.25)

# for j in range(steps):
#     XYZ2[j+1] = XYZ2[j] + Thomas(XYZ2[j],b,j) * dt

# ax = plt.figure().add_subplot(projection='3d')  
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

# print(xyzs.T)

"""
Notes--
For a b value of 0.208186, no matter the starting point, the system always falls back into the same exact orbit.
I think in this case, the attractor itself is the orbit the point falls into. The wiki describes it as having become chaotic.

There are TWO attractors, which are symmetrical to eachother (in every regard?).

"""
colors = plt.cm.twilight_shifted(XYZvelo)
# colors = plt.cm.magma(XYZvelo)

XYZ = XYZ.T

# line_segments = LineCollection(XYZ,linewidths=(0.5, 1, 1.5, 2),colors=colors,linestyle='solid')

# ax.add_collection(line_segments)

# line_segments = Line3DCollection(*XYZ,lw=0.5)

# ax.add_collection(line_segments)

ax.scatter(*XYZ,color=colors,s=0.01)
# ax.set_facecolor('black')

# ax.plot(*XYZ,color='cyan',lw=0.5)
# ax.plot(XYZ[0,:],XYZ[1,:],XYZ[2,:],color=colors[0])
# ax.set_prop_cycle('color',XYZvelo)
# ax.plot(*XYZ2.T, color='purple',lw=0.5)
# ax.scatter(*XYZ.T, color='magenta',s=0.01)    
# ax.plot(*XYZ2.T, '.', color='cyan', markersize= 0.01)

# ax.set_xlabel("X Axis")
# ax.set_ylabel("Y Axis")
# ax.set_zlabel("Z Axis")

# ax.axis('off')
# ax.set_facecolor('black')
ax.set_title("Thomas’ Cyclically Symmetric Attractor")

plt.show()