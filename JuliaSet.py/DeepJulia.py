import matplotlib.pyplot as plt
import numpy as np
import pygnuplot 
import h5py
import time
start_time = time.time()

f = h5py.File("JuliaSet","w")

size = 500
arrayparam = 2
thresh1 = 2
thresh2 = 2
plane = 1.25 #2*plane by 2*plane spac
precision = 25
accuracy = 100
julia = np.zeros((size,size), dtype = complex)
c1 = 0.6+0.55j 

dsetmap = f.create_dataset("map",data = np.zeros((size*2, size*2)),dtype=int)

x = np.round(np.linspace(-(plane), (plane), size*arrayparam, dtype=complex), precision)
y = np.round(np.linspace(-(plane)*1j,(plane)*1j, size*arrayparam, dtype=complex), precision)
# temparr = np.zeros((size,size),dtype = );

dsetinputs = f.create_dataset("inputs",data = (x + y[:, np.newaxis]),dtype = complex)

def iterate(z: complex, c: complex,count:int =0) -> complex:
    # zf = (np.vectorize(z**5 + c))
    zf:complex = z**5 + c
    dsetmap[np.absolute(zf) > complex(thresh2,thresh2)] = count
    if count == accuracy:
        return zf
   
    return (iterate(zf,c1,count+1))

# print(dsetinputs[0:size,0:size])


julia = iterate(dsetinputs[()], c1)
 
fig, ax = plt.subplots()
plt.imshow(dsetmap[()],cmap= plt.cm.magma)
ax.invert_yaxis()
plt.axis('off')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
 
 