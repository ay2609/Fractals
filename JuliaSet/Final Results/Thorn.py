import numpy as np
import matplotlib.pyplot as plt

box = 3
size = 700
recur = 250

x = np.linspace(-box, box, size)
y = np.linspace(-box, box, size)

X, Y = np.meshgrid(x, y)

mapp = np.zeros((size, size), dtype=int)

# cx, cy = 0.102, -0.04
cx, cy = 0.662, 1.086

def Iterate(X, Y, count=0):
    Xsave = X

    mask_1 = (abs((X + (Y * 1j))) < 1000)
    mask_2 = (mapp == 0)

    X[mask_1 & mask_2] = ((X / np.cos(Y)) + cx)[mask_1 & mask_2]
    Y[mask_1 & mask_2] = ((Y / np.sin(Xsave)) + cy)[mask_1 & mask_2]

    mask_3 = (abs((X + (Y * 1j))) > 1000)

    mapp[mask_2 & mask_3] = count

    if count == recur:
        return

    return Iterate(X, Y, count + 1)

Iterate(X, Y)

plt.imshow(mapp, plt.cm.bone, extent=[-box, box, -box, box])

plt.show()
