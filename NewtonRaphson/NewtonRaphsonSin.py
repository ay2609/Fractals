import matplotlib.pyplot as plt
import numpy as np
import math
import time
import sympy
import sys
# import pygnuplot

## 3-4 Hours

sys.setrecursionlimit(1500)

size = 1000
accuracy = 900 #892
# accuracy = 500
precision = 50


x = sympy.symbols('x')

PLANE_X = 0.4
PLANE_Y = 0.4

step = int(15000/size)

if step < 1:
    step = 1

n = 0

map = np.zeros((size, size), dtype=int)
outputs = np.zeros((size,size),dtype=complex)

def iterate(x: complex, accuracy, i,step,count: int =0,) -> complex:
    old_save = map[i:i+step,:]

    # x = np.round((x- ((np.sin(x) - 1)/(np.cos(x)))),precision)
    # x = np.round((x- ((np.sin(x))/(np.cos(x)))),precision)
    x = np.round((x- ((np.cos(x))/(-np.sin(x)))),precision)

    # x = np.round((x- (((x**2) * np.cos(x))/(2*x*np.cos(x) - (x**2) * np.sin(x)))),precision)
    

    # x = np.round((x- ((np.sin(x)/x)/((np.cos(x)/x)-(np.sin(x)/x**2)))),precision)


    # d/dx of sinx/x = (cosx/x - sinx/x^2)
    
    
    new_save = map[i:i+step,:]
    

    # For sin(z) -1 
    # mask_1 = (np.isclose(np.mod(abs(x),math.pi/2),0,atol=0.0040))
    # mask_2 = (np.isclose(np.cos(x),0,atol=0.008))
    # mask_2_5 = (np.isclose(np.imag(x),0,atol=0.008))

    # For sin(z)
    # mask_1 = (np.isclose(np.mod(abs(x),math.pi),0,atol=0.0055)) #option 1
    # mask_1 = (np.isclose(np.mod(np.real(x),math.pi),0,atol=0.0073)) #option 2
    # mask_2 = (np.isclose(np.imag(x),0,atol=0.005 ))

    # For cos(z)
    mask_1 = (np.isclose(np.mod(abs(x),math.pi/2),0,atol=0.0055))
    # mask_2 = (np.isclose(np.imag(x),0,atol=0.011))

    # For everything
    mask_3 = (map[i:i+step,:] == 0)


    
    # Mapped based on iteration
    map[i:i+step,:][mask_1 & mask_3] = count
    # map[i:i+step,:][mask_1 & mask_2 & mask_3] = count

    # Mapped based on distance
    # map[i:i+step,:][mask_1 & mask_3] = (np.abs(np.round(np.real(x)/math.pi,0)))[mask_1 & mask_3]
    # map[i:i+step,:][mask_2 & mask_2_5 & mask_3] = (np.abs(np.round(np.real(x)/math.pi,0)))[mask_2 & mask_2_5 & mask_3] 

    if count % 2 == 0:
        if all(new_save[old_save == new_save]) == True:
            return x

    if count == accuracy:
        return x
   
    return (iterate(x, accuracy,i, step,count+1))
 

def run(size, accuracy, step, precision, mapp):
    """
    Generate a grid of complex numbers and iterate the Julia set function on it.
    """

    # Create a grid of complex numbers
    x = np.round(np.linspace(-PLANE_X + (math.pi*n)/2, PLANE_X + (math.pi*n)/2, size, dtype=complex), precision)
    # x = np.round(np.linspace(-PLANE_X, PLANE_X, size, dtype=complex), precision)
    y = np.round(np.linspace(-PLANE_Y*1j, PLANE_Y*1j, size, dtype=complex), precision)
    inputs = x + y[:, np.newaxis]
   
    #############################################thread here##############################

    # Create an AxesImage object and initialize it with the data in the grid

    # Iterate the Julia set function on the grid
    
    for i in range(0, size, step):
        outputs[i:i+step,:] = iterate(inputs[i:i+step,:], accuracy, i, step)

    # diff1 = r1 - np.round(outputs,3)
    # diff2 = r2 - np.round(outputs,3)
    # diff3 = r3 - np.round(outputs,3)
    # diff4 = r4 - np.round(outputs,3)
    # diff5 = r5 - np.round(outputs,3)

    # map[diff1==(0+0j)] = 1
    # map[diff2==(0+0j)] = 2
    # map[diff3==(0+0j)] = 3
    # map[diff4==(0+0j)] = 4
    # map[diff5==(0+0j)] = 5
    
    # Plot the Julia set using imshow
    fig, ax = plt.subplots()
    fig.set_size_inches((6.5,6))
    print("shape = ",np.shape(mapp));
    # plt.imshow(mapp,cmap=plt.cm.inferno)
    # plt.imshow(mapp,cmap= plt.cm.twilight_r)
    plt.imshow(mapp,cmap= plt.cm.prism)
    # plt.imshow(mapp,cmap= plt.cm.gist_rainbow)


    print(np.amax(mapp))

    ax.invert_yaxis()   
    plt.axis('off')
#can make it so that you check the map array for the highest value and it'll give you the most optimized accuracy,
#since after a certain point every value for your thing will have reached a root by some number




 
    
start_time = time.time()
print("----------\nsize: {} \nstep: {} \naccuracy: {} \nprecision: {}".format(size,step,accuracy,precision)) 
run(size, accuracy, step, precision, map)
print("--- %s seconds ---" % np.round((time.time() - start_time),2))

# plt.savefig('FractalPics/X2COS_3',dpi=1000,bbox_inches='tight',pad_inches=0)

plt.show()
 
 
