import numpy  as np
import matplotlib.pyplot as plt
from skimage.transform import resize


# mapp = np.load('mapp.npy')
# mapp = np.load('7500Mapp.npy')



# step = int((np.shape(mapp)[0])/15)

# for i in range(0,int(np.shape(mapp)[0]),int((np.shape(mapp)[0])/15)):
#     mapp[i:i+step,:] = (np.sin((mapp[i:i+step,:]))**2)*100

mapp = np.load('MandelbrotUnderlay.npy')
mapp = resize(mapp, (2000,2000))
mapp = mapp*(10**10)



fig,ax = plt.subplots()
plt.imshow(mapp,cmap=plt.cm.bone)
ax.invert_yaxis()
plt.axis('off')


plt.show()