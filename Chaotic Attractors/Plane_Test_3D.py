import numpy as np
import matplotlib.pyplot as plt
import math
import time
start_time = time.time()

# 6-8 Hours
def EuclidDist(x,y):
    r = np.sqrt(x**2 + y**2)
    return r

def VecDist(vec):
    x,y,z = vec
    r = np.sqrt(x**2 + y**2 + z**2)
    return r

def rotate(x,y,degr):
    rad = degr*(math.pi/180)

    xp = x*np.cos(rad) - y*np.sin(rad)
    yp = x*np.sin(rad) + y*np.cos(rad)

    return xp,yp

def rotateX(vec,degr):
    #Rotate about the X axis (y and z)
    x,y,z = vec
    
    rad = degr*(math.pi/180)

    xp = x
    
    yp = y*np.cos(rad) - z*np.sin(rad)

    zp = y*np.sin(rad) + z*np.cos(rad)

    return (xp,yp,zp)

def rotateY(vec,degr):
    #Rotate about the Y axis (x and z)
    x,y,z = vec
    
    rad = degr*(math.pi/180)

    xp = x*np.cos(rad) - z*np.sin(rad)
    
    yp = y

    zp = x*np.sin(rad) + z*np.cos(rad)

    return (xp,yp,zp)

def rotateZ(vec,degr):
    #Rotate about the Z axis (x and y)
    x,y,z = vec
    
    rad = degr*(math.pi/180)
    
    xp = x*np.cos(rad) - y*np.sin(rad)

    yp = x*np.sin(rad) + y*np.cos(rad)
    
    zp = z

    return (xp,yp,zp)

def RotateSysX(vecx,vecy,vecz,degr):
    vecx = rotateX(vecx,degr)
    vecy = rotateX(vecy,degr)
    vecz = rotateX(vecz,degr)
    return vecx,vecy,vecz

def RotateSysY(vecx,vecy,vecz,degr):
    vecx = rotateY(vecx,degr)
    vecy = rotateY(vecy,degr)
    vecz = rotateY(vecz,degr)
    return vecx,vecy,vecz

def RotateSysZ(vecx,vecy,vecz,degr):
    vecx = rotateZ(vecx,degr)
    vecy = rotateZ(vecy,degr)
    vecz = rotateZ(vecz,degr)
    return vecx,vecy,vecz


size = 50

rdist = 6
Xrot = 0
Yrot = 0
Zrot = 0

Xdisp = -4.5
Ydisp = -4
Zdisp = -4

#       x,y,z       #
xvnorm = [0.5,0,0]
yvnorm = [0,0.5,0]
zvnorm = [0,0,0.5]

xvec = [rdist,0,0]
yvec = [0,rdist,0]
zvec = [0,0,rdist]


# xvec = rotateZ(xvec,Zrot)

xvec,yvec,zvec = RotateSysX(xvec,yvec,zvec,Xrot)
xvec,yvec,zvec = RotateSysY(xvec,yvec,zvec,Yrot)
xvec,yvec,zvec = RotateSysZ(xvec,yvec,zvec,Zrot)


# yvec = np.cross(zvec,xvec)

# print(VecDist(xvec),VecDist(yvec),VecDist(zvec))

# if (np.dot(xvec,zvec) == 0).all():
#     print("Is Orthog")

x = np.linspace((0,0,0), (xvec[0],xvec[1],xvec[2]), size, dtype=float)
y = np.linspace((0,0,0), (yvec[0],yvec[1],yvec[2]), size, dtype=float)
z = np.linspace((0,0,0), (zvec[0],zvec[1],zvec[2]), size, dtype=float)


xnorm = np.linspace((0,0,0), (xvnorm[0],xvnorm[1],xvnorm[2]), size, dtype=float)
ynorm = np.linspace((0,0,0), (yvnorm[0],yvnorm[1],yvnorm[2]), size, dtype=float)
znorm = np.linspace((0,0,0), (zvnorm[0],zvnorm[1],zvnorm[2]), size, dtype=float)


rx = VecDist((x[:,0],x[:,1],x[:,2]))

ry = VecDist((y[:,0],y[:,1],y[:,2]))

rz = VecDist((z[:,0],z[:,1],z[:,2]))


# deg = np.arcsin(xvec[1]/EuclidDist(xvec[0],xvec[1]))

# print(deg)
# deg = 45


fig,ax = plt.subplots(subplot_kw=dict(projection='3d'))

# fig,ax = plt.subplots()

#r mesh x and y
rmx,rmy,rmz = np.meshgrid(rx,ry,rz)

# print(np.shape(rmx),np.shape(rmy),np.shape(rmz))

#apply rotations

rmy,rmz = rotate(rmy,rmz,Xrot)
rmx,rmz = rotate(rmx,rmz,Yrot)
rmx,rmy = rotate(rmx,rmy,Zrot)

#apply linear transformations/affine transformations (?)

#vectors
x[:,0],y[:,0],z[:,0] = x[:,0] + Xdisp,y[:,0] + Xdisp,z[:,0] + Xdisp
x[:,1],y[:,1],z[:,1] = x[:,1] + Ydisp,y[:,1] + Ydisp,z[:,1] + Ydisp
x[:,2],y[:,2],z[:,2] = x[:,2] + Zdisp,y[:,2] + Zdisp,z[:,2] + Zdisp

#gridspace array
rmx = rmx + Xdisp
rmy = rmy + Ydisp
rmz = rmz + Zdisp




# print(np.shape(x),np.shape(y))


#-- TCSA


def Thomas(xyz, b, i):
    x, y, z = xyz
    
    dx = np.sin(y) - b*x
    dy = np.sin(z) - b*y
    dz = np.sin(x) - b*z

    XYZvelo[i] = np.sqrt((dx**2) + (dy**2) + (dz**2))


    return np.array([dx,dy,dz])

b = 0.208186
dt = 0.01
steps = 20000

XYZvelo = np.empty((steps+1))

XYZ = np.empty((steps+1,3))
XYZ[0] = (-0.33,-0.1,-0.25)

for i in range(steps):
    XYZ[i+1] = XYZ[i] + Thomas(XYZ[i],b, i) * dt

XYZvelo = XYZvelo/max(XYZvelo)
XYZvelo = np.round(XYZvelo,3)

colors = plt.cm.twilight_shifted(XYZvelo)

XYZ = XYZ.T

ax.scatter(*XYZ,color=colors,s=0.01)


#--



# if (CoordGrid[0]==rmx).all():
#     print("TRUEE")

mappgrid = np.zeros((size,size,size),dtype=int)


TOL = 0.08

print("check1",np.round((time.time() - start_time),3))
# stepval = int(10000/size)
stepval = 5

for j in range(0,size,stepval):
    for i in range(steps+1):
        mask_1 = (np.isclose((rmx[j:j+stepval,:] - XYZ[0,i]),0,rtol=TOL,atol=TOL))
        mask_2 = (np.isclose((rmy[j:j+stepval,:] - XYZ[1,i]),0,rtol=TOL,atol=TOL))
        mask_3 = (np.isclose((rmz[j:j+stepval,:] - XYZ[2,i]),0,rtol=TOL,atol=TOL))
        mappgrid[j:j+stepval,:][mask_1 & mask_2 & mask_3] += 1
print("check2",np.round((time.time() - start_time),3))

mapp = np.zeros((size,size),dtype=int)
for m in range(size):
    for n in range(size):
        mapp[n,m] = np.sum(mappgrid[m,n,:])
print("check3",np.round((time.time() - start_time),3))



# print(np.shape(CoordGrid))


ax.plot(*x.T,color='cyan')
ax.plot(*y.T,color='red')   
ax.plot(*z.T,color='green')

ax.plot(*xnorm.T,color='black')
ax.plot(*ynorm.T,color='black')   
ax.plot(*znorm.T,color='black')

# mask_4 = (mappgrid > 0)

# ax.scatter(rmx[mask_4],rmy[mask_4],rmz[mask_4],color='blue',s=0.25)
# ax.scatter(rmx[0],rmy[0],rmz[0],color='purple',s=0.25)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
# ax.set_xlim(-5,5)
# ax.set_ylim(-5,5)
# ax.set_zlim(-5,5)

fig2,ax2 = plt.subplots()
plt.imshow(mapp,cmap=plt.cm.bone)

ax2.invert_yaxis()
plt.axis('off')

plt.show()
