import numpy as np
import matplotlib.pyplot as plt
import cmath

size = 500
rep = 100
precision = 3

# z = 13 + 13j


plane = 250

x = np.round(np.linspace(-(plane), (plane), size, dtype=complex), precision)
y = np.round(np.linspace((((plane)))*1j,-(plane)*1j, size, dtype=complex), precision)
inputs = x + y[:, np.newaxis]

mapp = np.zeros((size,size),dtype=int)
# mappy = np.zeros((size,size),dtype=int)

# print("INIT_Z:",z)

def iterate(z:int, count: int = 0):
    # z = 1/(z**2)
    # --- Odd Values
    mask_1 = (np.round(abs(z),0) % 2 == 1)
    # --- Even Values
    mask_2 = (np.round(abs(z),0) % 2 == 0)
    # --- Values that HAVE NOT reached one
    mask_3 = (np.round(z,2) != 1)
    # --- Values that HAVE reached one
    mask_4 = (np.round(z,2) == 1)
    # --- Change count in mapp only for values where that count is greater than the current count of mapp
    mask_5 = (count > mapp)
    # --- Dont remapp, unless 
    # mask_6_1 = (mapp == 0)

    z[mask_1 & mask_3] = (3*z +1)[mask_1 & mask_3]
    z[mask_2 & mask_3] = (z/2)[mask_2 & mask_3]

    mapp[mask_4 & mask_5] = count

    print(count)

    # if np.round(abs(z)) % 2 == 1:
    #     z = 3*z + 1
    # else:
    #     z /= 2
    



    # print("COUNT:",count," Z:",z)

    # if (np.round(z,2) == 1):
    #     return


    # if cmath.isclose(z, 0,rel_tol=0.000001,abs_tol=0.000001):
    #     return

    # if abs(z) > 1000:
        # return
    
    if count == rep:
        return
    
    return iterate(z,count+1)

def run(z):
    x_int = np.real(z)
    y_int = np.imag(z)
    # print(x_int)
    # print(y_int)

    iterate(x_int)
    iterate(y_int)

    plt.imshow(mapp,cmap=plt.cm.bone)
    plt.axis('off')

    # fincount = 0
    # if count_x > count_y:
    #     fincount = count_x
    # else:
    #     fincount = count_y

    # print("fincount",fincount)
    

run(inputs)
plt.show()


# iterate(z)
