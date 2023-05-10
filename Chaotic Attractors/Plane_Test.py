import numpy as np
import matplotlib.pyplot as plt
import math

def EuclidDist(x,y):
    r = np.sqrt(x**2 + y**2)
    return r

def rotate(x,y,degr):
    rad = degr*(math.pi/180)

    xp = x*np.cos(rad) - y*np.sin(rad)
    yp = x*np.sin(rad) + y*np.cos(rad)

    return xp,yp




#       x,y,z       #
xvec = [1,1,0]
zvec = [0,0,-1]
yvec = np.cross(xvec,zvec)

# print(yvec)





x = np.round(np.linspace((0,0), (xvec[0],xvec[1]), 15, dtype=float), 5)
y = np.round(np.linspace((0,0), (yvec[0],yvec[1]), 15, dtype=float), 5)


# X,Y = np.meshgrid(x[:,0],x[:,1])
# X2,Y2 = np.meshgrid(y[:,0],y[:,1])

rx = EuclidDist(x[:,0],x[:,1])

ry = EuclidDist(y[:,0],y[:,1])

if ((rx==ry).all()):
    print("same dist")




deg = np.arcsin(xvec[1]/EuclidDist(xvec[0],xvec[1]))

print(deg)
# deg = 45

rmx,rmy = np.meshgrid(rx,ry)

rmx,rmy = rotate(rmx,rmy,deg*(180/math.pi))

print(np.shape(x[:,:]),np.shape(y[:,:]))



# fig,ax = plt.subplots(subplot_kw=dict(projection='3d'))
fig,ax = plt.subplots()

# plt.figure(figsize=(5,5))

plt.xlim([-3,3])
plt.ylim([-3,3])

ax.plot(*x.T)
ax.plot(*y.T)

ax.scatter(rmx,rmy,color='purple',s=0.25)

# ax.scatter(X,Y,color='cyan',s=0.25)
# ax.scatter(X2,Y2,color='magenta',s=0.25)


plt.show()