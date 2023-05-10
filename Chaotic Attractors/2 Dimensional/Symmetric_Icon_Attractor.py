import numpy as np
import matplotlib.pyplot as plt
import math

#work
# labgod = (-2.5,5,-1.9,1,0.188,5) #ehh
# labgod = (1.56 ,-1 ,0.1 ,-0.82 ,0.12 ,3) #good
# labgod = (-1.806 ,1.806 ,0 ,1 ,0 ,5) #ehh-good
# labgod = (-2.195 ,10 ,-12 ,1 ,0 ,3) #good
# labgod = (2.5 ,-2.5 ,0 ,0.9 ,0 ,3) #mid
# labgod = (-2.7 ,5 ,1.5 ,1.0 ,0 ,6) #good
labgod = (-2.32 ,2.32 ,0 ,0.75 ,0 ,5) #ehh
# labgod = (1.455 ,-1 ,0.03 ,-0.8 ,0 ,3) #good

# labgod = (2.39 ,-2.5 ,-0.1 ,0.9 ,-0.15 ,16) #ehh-good

#dont work
# labgod = (-2.5, -0.1, 0.9, -0.15, 2.39, 16)
# labgod = (-2.5, 0.0, 0.9, 0.0, 2.5, 3)

def SymIcon(xy, labgod):
    x, y = xy
    l,a,b,g,o,d = labgod

    zzbar = x**2 + y**2
    p = a*zzbar + l
    zreal,zimag = x,y 

    for m in range(1, d-1):
        za,zb = zreal * x - zimag * y, zimag * x + zreal * y
        zreal,zimag = za,zb

    zn = x*zreal - y*zimag
    p += b*zn

    dx=p*x+g*zreal-o*y
    dy=p*y-g*zimag+o*x
    
    return np.array([dx,dy])


# steps = 5000000
steps = 1000000

XY = np.empty((steps+1,2))
XY[0] = (0.1,0.1)



for i in range(steps):
    # print(i)
    XY[i+1] = SymIcon(XY[i],labgod)


XY = XY.T

fig,ax = plt.subplots()

fig.set_facecolor("black")
# fig.set_facecolor("white")


coloring = plt.cm.gist_rainbow(np.linspace(0,1,steps+1))

# coloring = plt.cm.inferno(np.linspace(0,1,steps+1)) #Mid
# coloring = plt.cm.magma(np.linspace(0,1,steps+1)) #EHH
# coloring = plt.cm.twilight_shifted(np.linspace(0,1,steps+1)) #trash


plt.scatter(*XY,s = 0.05,alpha = 0.2,linewidths=0,color=coloring)
plt.axis('off')

plt.show()