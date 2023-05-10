import matplotlib.pyplot as plt
import numpy as np
import sympy
import time
import cmasher as cmr
# import pygnuplot

## 7-10 Hours

disp = 0

size = 2000
precision = 50
plane = 0.75
accuracy = 750
PLANE_X = 1.25
PLANE_Y = 1.25
step = int(20000/size)

x = sympy.symbols('x')

# solutions = sympy.solve(5*x**7  + 3*x**5 - 27*x**2 + 365,x)
# solutions = sympy.solve(x**3 -  1,x)
solutions = sympy.solve(x**5 + 1,x) 

for i in range(np.shape(solutions)[0]):
    solutions[i] = sympy.simplify(solutions[i])
    solutions[i] = complex(solutions[i].evalf())
solutions = np.round(solutions,7)





if step < 1:
    step = 1




map = np.zeros((size, size), dtype=int)
fmap = np.zeros((size, size), dtype=int)
outputs = np.zeros((size,size),dtype=complex)

def iterate(x: complex, accuracy, i,step,count: int =0,) -> complex:
    old_save = map[i:i+step,:]

    # xn1 = np.round((x - ((6*x**3 - 3*x**2 + 12*x + 6)/(18*x**2 - 6*x + 12))),precision)
    # xn1 = np.round((x- ((x**3-1)/(3*x**2))),precision)
    xn1 = np.round((x- ((x**5+1)/(5*x**4))),precision)
    # xn1 = (x - (f(x))/(f2(x))).round(precision)

    # xn1 = np.round(x - (5*x**7  + 3*x**5 - 27*x**2 + 365)/(35*x**6  + 15*x**4 - 54*x),precision)

    
    
    new_save = map[i:i+step,:]

    mask_1 = map[i:i+step,:]==0
    mask_a = np.isclose(xn1-solutions[0],0,atol=0.000015)
    map[i:i+step,:][mask_a & mask_1] = count
    mask_b = np.isclose(xn1-solutions[1],0,atol=0.000015)
    map[i:i+step,:][mask_b & mask_1] = count
    mask_c = np.isclose(xn1-solutions[2],0,atol=0.000015)
    map[i:i+step,:][mask_c & mask_1] = count
    mask_d = np.isclose(xn1-solutions[3],0,atol=0.000015)
    map[i:i+step,:][mask_d & mask_1] = count
    mask_e = np.isclose(xn1-solutions[4],0,atol=0.000015)
    map[i:i+step,:][mask_e & mask_1] = count
    


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
    x = np.round(np.linspace(-(PLANE_X) + disp, (PLANE_X) + disp, size, dtype=complex), precision)
    y = np.round(np.linspace(-(PLANE_Y)*1j, (PLANE_Y)*1j, size, dtype=complex), precision)
    inputs = x + y[:, np.newaxis]
   
    #############################################thread here##############################

    # Create an AxesImage object and initialize it with the data in the grid

    # Iterate the Julia set function on the grid
    
    for i in range(0, size, step):
        outputs[i:i+step,:] = iterate(inputs[i:i+step,:], accuracy, i, step)


    fig, ax = plt.subplots()

    cmaplist = ('cmr.ember','cmr.bubblegum','cmr.gem','cmr.horizon','cmr.tropical','cmr.savanna','cmr.gothic')

    for i in range(np.shape(solutions)[0]):
        mask = np.isclose(outputs-solutions[i],0,atol=0.000015)
        fmap[mask] = i
        map1 = np.ma.masked_array(map, fmap!=i)
        # cmap = plt.get_cmap(cmaplist[i])
        cmap = plt.get_cmap('inferno')
        ax.imshow(map1,cmap=cmap,interpolation='none')
    
    ax.invert_yaxis() 
    plt.axis('off')


start_time = time.time()
print("----------\nsize: {} \nstep: {} \naccuracy: {} \nprecision: {}".format(size,step,accuracy,precision)) 
run(size, accuracy, step, precision, map)
print("--- %s seconds ---" % np.round((time.time() - start_time),2))

# plt.savefig('FractalPics/X5_2',dpi=1000,bbox_inches='tight',pad_inches=0)
5
plt.show()
