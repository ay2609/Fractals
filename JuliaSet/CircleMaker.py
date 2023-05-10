import numpy as np
from Iterate import PLANE_X,PLANE_Y
import matplotlib.pyplot as plt
import cmath

# 3-4 Hours

size1 = 1024
precision = 50
mapp = np.zeros((size1,size1))

x = np.round(np.linspace(-(PLANE_X), (PLANE_X), size1, dtype=complex), precision)
y = np.round(np.linspace(-(PLANE_Y)*1j, (PLANE_Y)*1j, size1, dtype=complex), precision)
inputs = x + y[:, np.newaxis]

# print(inputs[0,1023])
vector = np.vectorize(cmath.isclose)
# mapp[vector((np.imag(inputs)**2 + np.real(inputs)**2 - 1),0,rel_tol=0.00155,abs_tol=0.00155)] = 1
mapp[vector((np.imag(inputs)**2 + np.real(inputs)**2 - 1),0,rel_tol=0.02,abs_tol=0.02)] = 1
np.save('mapp.npy',mapp)
fig,ax = plt.subplots()

# mapp[234,:] = 1
# np.save('mapp.npy',mapp)

plt.axis('off')
plt.imshow(mapp,cmap=plt.cm.bone)
plt.show()
