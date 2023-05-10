
# # cmap = plt.cm.magma bone RdBu
# # cmap.set_under(0)
# # cmap.set_over(accuracy)
# # rgba = cmap(145)

import numpy as np
import matplotlib.pyplot as plt
import math
import cmasher as cmr

THRESHOLD = 2

PLANE_X = 1.25
PLANE_Y = 1.25

CONST_PLANE = 800
def calc(z:complex,c:complex):
    z_1 = ((z*z) + c)
    return z_1



def iterate(z, c, i, accuracy, precision, step, mapp, count=0):
    """
    Iterate the Julia set function on the input complex numbers.
    """
    # Save a copy of the current state of the map
    old_save = mapp[i:i+step,:]

    # Apply the Julia set function to the input complex numbers
    # z = 1/(z)
    z = (z**2 + c)
    # z = (1 - z**2)/(z - 0.01*z**2 + 0.005*z**3)
    # z = (1000*(1 - z))/(8 - 4*z + 2*z**2 - z**3)
    # z = (-1*z**2)/2 + (z**3)/3
    # vector = np.vectorize(calc)

    # z = vector(z,c)

    # z = np.round((z- ((z**5-1)/(5*z**4))),precision)
    # Create masks to identify diverged points and uncolored points
    mask_2 = (abs(z) > THRESHOLD)
    mask_3 = (mapp[i:i+step,:] == 0)
    
    # Color the points that have diverged and are not already colored
    # if count == accuracy:
    #     mapp[i:i+step,:][mask_2 & mask_3] = 1
   
    if count < accuracy:
        mapp[i:i+step,:][mask_2 & mask_3] = count
    elif count == accuracy:
        mapp[i:i+step,:][mask_3] = accuracy
        # mapp[i:i+step,:][mask_3] = 0
    
    # Create a new copy of the map to check for convergence
    new_save = mapp[i:i+step,:]

    # If the map has not changed, stop iterating
    if (old_save == new_save).all() == True & count > 25:
        return 


    # If the maximum number of iterations has been reached, stop iterating
    if count == accuracy:
        # print("z:",z)
        return

    # Recursively call the function to continue iterating
    return iterate(z, c, i, accuracy, precision, step, mapp, count+1)





def run(size_1, size_2, accuracy, step, precision, c, mapp):
    """
    Generate a grid of complex numbers and iterate the Julia set function on it.
    """
    # Create a grid of complex numbers
    x = np.round(np.linspace(-(PLANE_X), (PLANE_X), size_2, dtype=complex), precision)
    y = np.round(np.linspace(-(PLANE_Y)*1j, (PLANE_Y)*1j, size_1, dtype=complex), precision)
    inputs = x + y[:, np.newaxis]
   
    
    # Create an AxesImage object and initialize it with the data in the grid

    # Iterate the Julia set function on the grid
    
    # print("inputs before:", inputs)

    for i in range(0, size_1, step):
        iterate(inputs[i:i+step,:], c, i, accuracy, precision, step, mapp)
    
    # print("inputs after:", inputs) #not sure if it changes


    # Plot the Julia set using imshow
    fig, ax = plt.subplots()
    # print("shape = ",np.shape(mapp));
    # plt.imshow(mapp,cmap=plt.cm.bone)
    
    # plt.imshow(mapp,cmap=cmr.sepia)
    # plt.imshow(mapp,cmap=cmr.ocean)
    # plt.imshow(mapp,cmap=cmr.lilac)
    # plt.imshow(mapp,cmap=cmr.gothic)
    # plt.imshow(mapp,cmap=cmr.horizon)
    
    # plt.imshow(mapp,cmap= plt.cm.twilight_r)
    plt.imshow(mapp,cmap= plt.cm.inferno)
    
    ax.invert_yaxis()   
    plt.axis('off')




gr = (1 + np.sqrt(5)) / 2
# a = 15-15j
a = -0.33258 + 0.10324j
e = math.e

c = a
