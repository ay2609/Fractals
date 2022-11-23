import matplotlib.pyplot as plt
import numpy as np
import pygnuplot 
import h5py
import time
start_time = time.time()
f = h5py.File("JuliaSet","w")

size = 1000
arrayparam = 2
thresh1 = 2
thresh2 = 2
plane = 1.25 #2*plane by 2*plane spac
precision = 25
accuracy = 100
julia = np.zeros((size,size), dtype = complex)
c1 = 0.6+0.55j 

dsetmap = f.create_dataset("map",data = np.zeros((size*2, size*2)),dtype=int, chunks = (size,size))

x = np.round(np.linspace(-(plane), (plane), size*arrayparam, dtype=complex), precision)
y = np.round(np.linspace(-(plane)*1j,(plane)*1j, size*arrayparam, dtype=complex), precision)

dsetinputs = f.create_dataset("inputs",data = (x + y[:, np.newaxis]),dtype = complex, chunks = (size,size))
dsetoutputs = f.create_dataset("outputs",data = np.zeros((size*2, size*2),dtype=complex), dtype= complex, chunks = (size,size))

def iterate(z: complex, c: complex, i:int, k:int,dsetoutputs, dsetmap,count:int =0) -> complex:
    # zf = (np.vectorize(z**5 + c))
    zf:complex = z**5 + c
    dsetoutputs[i:i+size,k:k+size] = zf
    
    dsetmap[np.absolute(dsetoutputs) > complex(thresh2,thresh2)] = count
    if count == accuracy:
        return zf
   
    return (iterate(zf,c1, i, k, dsetoutputs[()],dsetmap[()],count+1))

# print(dsetinputs[0:size,0:size])

for i in range(0,size*arrayparam,size):
    for k in range(0,size*arrayparam,size):
        julia = iterate(dsetinputs[i:i+size,k:k+size], c1 , i , k, dsetoutputs[()], dsetmap[()])


fig, ax = plt.subplots()
plt.imshow(dsetmap[()],cmap= plt.cm.magma)
ax.invert_yaxis()
plt.axis('off')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
 
 