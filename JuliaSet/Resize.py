from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt
mapp = np.load('mapp.npy')
# # for dendrite
# mapp[mapp > 15] = 0
# mapp[mapp <=11] = 1

# # for filled in
# mapp[mapp > 0] = 12
# mapp[mapp == 0] = 1
# mapp[mapp == 12] = 0


# for resize
mapp[mapp > 0] = 1 

# # for prisoner sets
# mapp[mapp > 10] = 12
# mapp[mapp > 0] = 1

#Plot Original
fig1,ax1 = plt.subplots()
plt.imshow(mapp,cmap=plt.cm.magma)
plt.axis('off')
ax1.invert_yaxis()

#Print Original Shape
print("shape:", np.shape(mapp))

#Resize the image
mapp = resize(mapp, (np.shape(mapp)[0]*2,np.shape(mapp)[1]*2))
mapp = mapp*(10**10)

# for resize
mapp[mapp > 2.5] = 10
mapp[mapp<.8] = 10
mapp[mapp!=10] = 1
mapp[mapp==10] = 0

# # for dendrite
# mapp[mapp != 0] = 10
# mapp[mapp == 0] = 1
# mapp[mapp == 10] = 0


# # for non dendrite
# mapp[mapp == 0] = 0
# mapp[mapp <= 10] = 0
# mapp[mapp == 12] = 1


#Print New Shape
print("shape:", np.shape(mapp))

#Plot New
fig,ax = plt.subplots()
plt.imshow(mapp,cmap=plt.cm.bone)
plt.axis('off')
ax.invert_yaxis()
plt.show()

np.save('mapp.npy',mapp)

