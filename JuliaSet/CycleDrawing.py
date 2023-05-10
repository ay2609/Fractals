import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
# import cmath
import time

## 4-5 Hours

PLANE_X = 1.25
PLANE_Y = 1.25

THRESHOLD = 2

# MIN_ITER_CHECK = 10
size = 2000
precision = 3
accuracy = 100
TOL = 0.05
step = int(15000/size)

Underlay = np.load('MandelbrotUnderlay.npy')
#Resize the image
Underlay = resize(Underlay, (size,size))
Underlay = Underlay*(10**10)

Under_Mask = (Underlay > 3)




x = np.round(np.linspace(-(PLANE_X) - 0.6, (PLANE_X) - 0.6, size, dtype=complex), precision)
y = np.round(np.linspace(-(PLANE_Y)*1j, (PLANE_Y)*1j, size, dtype=complex), precision)
inputs = x + y[:, np.newaxis]

mapp = np.zeros((size,size), dtype=int)

mandelZ = np.zeros((size,size),dtype=complex)

juliaC = 0 + 0j

# vector = np.vectorize(cmath.isclose)

def iterateMandel(z:complex, c:complex, c_old:complex,accuracy:int,i, count:int = 0):
    
    #mask1 - for values that have left the boundary
    mask_1 = (np.absolute(z) < complex(THRESHOLD,THRESHOLD))
 
    # z = (z**2 + c)
    # z[mask_1] = (z**2 + c)[mask_1]
    z[Under_Mask[i:i+step,:] & mask_1] = (z**2)[Under_Mask[i:i+step,:] & mask_1]
    # z[Under_Mask[i:i+step,:]] = (z**2 + c)[Under_Mask[i:i+step,:]]


    # mask_1 = (np.absolute(z) < complex(THRESHOLD,THRESHOLD))

    #mask1.5 - for values above the threshhold)
    mask_1_5 = (np.absolute(z) > complex(THRESHOLD,THRESHOLD))
    #mask2 - for values that are close to their initial value
    mask_2 = (np.isclose((z - c_old),0,rtol=TOL))
    #mask3 - for values of mapp that have not been mapped
    # mask_3 = (mapp[i:i+step,:] == 0) #---------CHANGE WHEN IMPLEMENTING STEPPED INPUTS---------------#
    # mask_3 = (mapp == 0)

    mapp[i:i+step,:][mask_1_5] = 0
    # mapp[mask_1_5] = 0
    # if count > 0:
    mapp[i:i+step,:][mask_1 & mask_2] = 1
    # mapp[mask_1 & mask_2 & mask_3] = 1

    if (count > 100):
        if (mapp==0).all():
            return
    

    # print(count)
            
    # If the maximum number of iterations has been reached, stop iterating
    if count == accuracy:
        return

    # Recursively call the function to continue iterating
    return iterateMandel(z, c, c_old,accuracy,i,count+1)

start_time = time.time()
for i in range(0,size,step):
    print(i)
    iterateMandel(mandelZ[i:i+step,:],inputs[i:i+step,:],inputs[i:i+step,:],accuracy,i)
print("--- %s seconds ---" % np.round((time.time() - start_time),2))
# i = size-1
# iterateMandel(mandelZ,inputs,inputs,accuracy,i)

fig,ax = plt.subplots()

# np.save('MandelbrotUnderlay.npy',mapp)

plt.imshow(mapp,cmap = plt.cm.bone)
plt.axis('off')
ax.invert_yaxis()

plt.show()
    
    




# def iterateJulia(z:complex, c:complex, accuracy:int, count:int = 0):
#     pass
    
