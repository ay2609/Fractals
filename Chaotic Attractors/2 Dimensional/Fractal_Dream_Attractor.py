import numpy as np
import matplotlib.pyplot as plt

# abcd = (-0.966918 ,2.879879 ,0.765145 ,0.744728)
abcd = (-2.8276 ,1.2813 ,1.9655 ,0.597)


def Dream(xy, abcd):
    x, y = xy
    a, b, c, d = abcd
    
    dx = np.sin(b*y) + c*np.sin(b*x)
    dy = np.sin(a*x) + d*np.sin(a*y)
    # print(dy)
    return np.array([dx,dy])

dt = 1
steps = 1500000

XY = np.empty((steps+1,2))
XY[0] = (0.1,0.1)

for i in range(steps):
    XY[i+1] = Dream(XY[i],abcd) * dt


XY = XY.T

fig,ax = plt.subplots()

fig.set_size_inches((6.5,6))

fig.set_facecolor("black")

coloring = plt.cm.gist_rainbow(np.linspace(0,1,steps+1))

plt.scatter(*XY,s = 0.05,alpha = 0.2,linewidths=0,color=coloring)
plt.axis('off')

plt.show()