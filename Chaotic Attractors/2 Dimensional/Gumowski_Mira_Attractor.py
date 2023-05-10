import numpy as np
import matplotlib.pyplot as plt
import math
import random
import seaborn as sns

## 7-10 Hours

def EuclidDist(xy):
    x,y = xy
    r = np.sqrt(x**2 + y**2)
    return r

def func(x,a):
    # xp = (a*x) + 2*(1-a)*(x**2)*(1+(x**2))**-1    
    xp = a*x + 2*(1-a)*(x**2)*(1+(x**2))**-2
    return xp


# print(np.round(np.sin(2*math.pi),5))

# ab = (0.93,0.5)
# ab = (0.292,0.982) # galaxy orbit


# ab = (0.999,-0.999)

# ab = (-0.048,0.982) #cool 

# ab = (-0.292,0.982) #one i made
ab = (-0.192,0.982) ##og good one
# ab = (0.008,-0.7)
# ab = (0.6,.995)
def Mira(xy, ab):
    x, y = xy
    a, b = ab
    
    # dx = y + a*(1-(0.05*(y**2))) + func(x,b)
    # dy = -x + func(dx,b)
    
    dx = b*y + func(x,a)
    dy = func(dx,a) - x
    # print(dy)
    return np.array([dx,dy])


fig,ax = plt.subplots()
fig2,ax2 = plt.subplots()

steps = 1000
points = 100

ranje = 0.1



for j in range(1,points+1):
    print(j)
    XY = np.empty((steps+1,2))
    XY[0] = (random.uniform(-ranje,ranje),random.uniform(-ranje,ranje))
    DistArr = np.empty((steps,2))  

    # print("init",XY[0])

    # XY[0] = (,7.75)
    for i in range(steps):
        XY[i+1] = Mira(XY[i],ab)
        DistArr[i] = i,EuclidDist(XY[i])
    

    
    # print("fin",XY[steps])
    
    XY = XY.T

    # print(np.shape(XY))
    ax.scatter(*XY, s=0.1,color="white",alpha=0.6,linewidths=0)
    ax2.plot(*DistArr.T,lw=0.3,alpha=0.2,color='{}'.format(j/(points*2)))

    

fig.set_facecolor("black")

ax.axis('off')

# plt.savefig('Gumowski_Mira.png')

fig.set_size_inches((6.5,6))




ax2.set_xlabel("Iters")
ax2.set_ylabel("Euclidean Distance From (0,0)")

plt.show()