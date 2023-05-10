import matplotlib.pyplot as plt
import numpy as np
import time
# import pygnuplot

## 15 Hours

size = 1000
precision = 50
plane = 0.75
accuracy = 150
PLANE_X = 1.25
PLANE_Y = 1.25
step = int(20000/size)
if step < 1:
    step = 1

# e = 2.718281828459045

r1, r2, r3 = 1-0j, np.round(-0.500000000000000 - 0.866025403784439j,3), np.round(-0.500000000000000 + 0.866025403784439j,3)
# r1, r2 ,r3, r4, r5 = np.round(-0.80902 - 0.58779j,3), np.round(-0.80902 + 0.58779j,3),np.round(0.30902 - 0.95106j,3),np.round(0.30902 + 0.95106j,3),np.round(1.00,2)
# print(r2,r3)

# r1, r2, r3 = np.round(-0.41922+0j,2), np.round(0.4596 - 1.4745j,2), np.round(0.4596 + 1.4745j,2)

map = np.zeros((size, size), dtype=int)
outputs = np.zeros((size,size),dtype=complex)
def iterate(x: complex, accuracy, i,step,count: int =0,) -> complex:
    old_save = map[i:i+step,:]
    # xn1 = np.round((x - ((6*x**3 - 3*x**2 + 12*x + 6)/(18*x**2 - 6*x + 12))),precision)
    xn1 = np.round((x- ((x**3-1)/(3*x**2))),precision)
    # xn1 = np.round((x- ((x**5-1)/(5*x**4))),precision)
    # xn1 = (x - (f(x))/(f2(x))).round(precision)
    # print("-------")
    # print("xn1",np.shape(xn1))
    # print("i",i)
    # print("map",np.shape(map))
    
    new_save = map[i:i+step,:]

    map[i:i+step,:][np.round(xn1,3)-r1==(0+0j)] = count
    xn1[np.round(xn1,3)-r1==(0+0j)] = 0 + 0j
    map[i:i+step,:][np.round(xn1,3)-r2==(0+0j)] = count
    xn1[np.round(xn1,3)-r2==(0+0j)] = 0 + 0j
    map[i:i+step,:][np.round(xn1,3)-r3==(0+0j)] = count
    xn1[np.round(xn1,3)-r3==(0+0j)] = 0 + 0j
    
    # map[i:i+step,:][np.round(xn1,3)-r4==(0+0j)] = count + 3
    # xn1[np.round(xn1,3)-r4==(0+0j)] = 0 + 0j
    # map[i:i+step,:][np.round(xn1,3)-r5==(0+0j)] = count + 4
    # xn1[np.round(xn1,3)-r5==(0+0j)] = 0 + 0j
    # print(count)
    
    if count % 2 == 0:
        if all(new_save[old_save == new_save]) == True:
            return xn1

    if count == accuracy:
        return xn1
   
    return (iterate(xn1, accuracy,i, step,count+1))
 

def run(size, accuracy, step, precision, mapp):
    """
    Generate a grid of complex numbers and iterate the Julia set function on it.
    """
    # Create a grid of complex numbers
    x = np.round(np.linspace(-(PLANE_X), (PLANE_X), size, dtype=complex), precision)
    y = np.round(np.linspace(-(PLANE_Y)*1j, (PLANE_Y)*1j, size, dtype=complex), precision)
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
    print("shape = ",np.shape(mapp));
    plt.imshow(mapp,cmap=plt.cm.inferno)
    # plt.imshow(mapp,cmap= plt.cm.twilight_r)
    # plt.imshow(mapp,cmap= plt.cm.inferno)
    
    ax.invert_yaxis()   
    plt.axis('off')
#can make it so that you check the map array for the highest value and it'll give you the most optimized accuracy,
#since after a certain point every value for your thing will have reached a root by some number


 
# f = lambda x1: x1**3 - 1
# f2 = lambda x1: 3*x1**2
#roots
# r1, r2, r3 = 1-0j, -.5 - .87j, -.5+.87j
 
    
start_time = time.time()
print("----------\nsize: {} \nstep: {} \naccuracy: {} \nprecision: {}".format(size,step,accuracy,precision)) 
run(size, accuracy, step, precision, map)
print("--- %s seconds ---" % np.round((time.time() - start_time),2))

# plt.imshow(map)
# plt.imshow(map,cmap= plt.cm.bone)
# ax.invert_yaxis()
# plt.axis('off')
plt.show()
 
 
 
##ROOT FINDER
 
 
###MAKE ANOTHER MATRIX FULL OF Y VALUES AND GRAPH THAT TOO, 3 D FUNCTIONS!!!!
### Graph Riemann Sum vector field
# https://www.youtube.com/watch?v=sD0NjbwqlYw
