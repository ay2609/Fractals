import numpy as np
import matplotlib.pyplot as plt
import math
import gmpy2

size  = 500
THRESHOLD = 1000
recur = 75

box = 1.5

x = np.linspace(-(box), (box), size, dtype=complex)
y = np.linspace((box)*1j, -(box)*1j, size, dtype=complex)
inputs = x + y[:, np.newaxis]

mapp = np.zeros((size,size),dtype = int)

def iterate(z, count = 0):
    print(count)

    mask_2 = (mapp == 0)
    # z[mask_2] = (((7*z + 2) - np.cos(math.pi*z)*(5*z+2))/4)[mask_2]
    
    z[mask_2] = (((7*z + 2) - np.round(math.e**(z*math.pi*1j),0)*(5*z+2))/4)[mask_2]
    # z[mask_2] = (((7*z + 2) - (math.e**(z*math.pi*1j))*(5*z+2))/4)[mask_2]

    mask_3 = (abs(z) > THRESHOLD)
    mapp[mask_2 & mask_3] = count

    if (count == recur):
        return

    return iterate(z, count+1)

iterate(inputs)


plt.imshow(mapp, cmap = plt.cm.magma, extent = [-box,box,-box,box])
plt.show()
