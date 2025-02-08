import matplotlib.pyplot as plt
import numpy as np
import cmasher as cmr
import warnings

# 5-10 Hours

# warnings.filterwarnings("ignore")
# import symengine as sym
# def mapcolor(p: complex, count: int, accuracy: int) -> int:
size = 200
mapp = np.zeros((size, size), dtype=int)
thresh1 = 1000
thresh2 = 1000  # manipulate these 2 with c**x to get varying results
gr = (1 + np.sqrt(5)) / 2

# xdisp = -120
xdisp = -.6
# xdisp = 0
ydisp = 0
# plane = 10
plane = 1.25
precision = 50


def iterate(x: complex, c: complex, count: int = 0, accuracy=900) -> complex:
    mask_1 = (abs(x) < thresh1)
    # x[mask_1] = (c ** x)[mask_1]
    xn1 = (x**2) + c
    # x = (np.abs(x.real) + 1j * np.abs(x.imag))**2 + c

    # mask_1 = (abs(x) < thresh1)
    # x[mask_1] = (x**2 + c)[mask_1]
    # x[mask_1] = (c**x)[mask_1]

    # xn1 = x**2 + (1/x) + c
    # xn1 = (1000*(1 - x))/(8 - 4*x + 2*x**2 - x**3) + c
    # mapp[np.absolute(xn1) > complex(thresh2,thresh2)] = count
    # x[np.absolute(xn1) > complex(thresh1,thresh1)] = 0 + 0j
    # xn1[np.absolute(xn1) > complex(thresh1,thresh1)] = 0 + 0j
    # c[np.absolute(xn1) > complex(thresh1,thresh1)] = 0 + 0j
    # print(xn1)
    # xn1 > 100+100j

    # check each iteration when a value has reached past a certain threshold, in which case you exempt it from continuing
    # iteration by setting its input and mandel array value back to 0 like in newtonraphson code,
    # assign it a value from counter to simulate shoot off speed

    mask2 = (abs(x) > thresh2)
    mask3 = (mapp == 0)

    if (count < accuracy):
        mapp[mask2 & mask3] = count
    elif (count == accuracy):
        # mapp[i:i+step,:][mask3] = accuracy
        mapp[mask3] = 0

    if count == accuracy:
        # print("z:",xn1)
        return x

    return (iterate(x, inputs, count + 1))


mandel = np.zeros((size, size), dtype=complex)

x = np.round(np.linspace(-(plane) + xdisp, (plane) + xdisp, size, dtype=complex), precision)
y = np.round(np.linspace(((-(plane) + ydisp)) * 1j, (plane + ydisp) * 1j, size, dtype=complex), precision)

inputs = x + y[:, np.newaxis]

iterate(mandel, inputs)

# map[mandel<10] = 1
# map[map == 0] = 2
# map[map == 1] = 0


fig, ax = plt.subplots()
# cmap = plt.get_cmap('prism')
# plt.imshow(mapp,cmap=cmap)
# plt.imshow(mapp,cmap=plt.cm.rainbow)

# plt.imshow(mapp,cmap=plt.cm.YlOrRd)
# plt.imshow(mapp,cmap=plt.cm.bone) #bone

plt.imshow(mapp, cmap=plt.cm.prism)
plt.axis('off')

# plt.savefig('FractalPics/Tetration',dpi=1000,bbox_inches='tight',pad_inches=0)

# ax.invert_yaxis()

plt.show()

# np.save('mapp.npy',mapp)


###MAKE ANOTHER MATRIX FULL OF Y VALUES AND GRAPH THAT TOO, 3 D FUNCTIONS!!!!
### Graph Riemann Sum vector field
# https://www.youtube.com/watch?v=sD0NjbwqlYw
