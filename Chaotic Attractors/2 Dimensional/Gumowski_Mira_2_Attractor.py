import numpy as np
import matplotlib.pyplot as plt
import math
import random




def func(x,a):
    # xp = a*x + ((2*(1-a)*(x**2))/(1+ x**2)**2)
    xp = a*x + 2*(1-a)*(x**2)*(1+(x**2))**-2
    # xp = a*x + ((2*(1-a)*(x**2))/(1+ x**2))
    return xp


# print(np.round(np.sin(2*math.pi),5))

# ab = (0.31,1.0)
# ab = (-0.192,0.982)
ab = (0.008,-0.7)

def Mira(xy, ab):
    x, y = xy
    a, b = ab
    
    dx = b*y + func(x,a)
    dy = -x + func(dx,a)
    # print(dy)
    return np.array([dx,dy])

fig,ax = plt.subplots()

steps = 5000
ranje = 10

for j in range(250):
    XY = np.empty((steps+1,2))
    XY[0] = (random.uniform(-ranje,ranje),random.uniform(-ranje,ranje))
    # XY[0] = (0.,0.5)
    for i in range(steps):
        XY[i+1] = Mira(XY[i],ab)
    XY = XY.T
    # print(np.shape(XY))
    plt.scatter(*XY, s=0.2,color="black",linewidths=0)
    print(j)

# fig.set_facecolor("black")

plt.axis('off')

fig.set_size_inches((6.5,6))

plt.show()