import numpy as np
import matplotlib.pyplot as plt




# abcd = (-2, 1.6, 1.0, 0.7)
# abcd = (2.1, 1.7, -0.5, -1)
# abcd = (-1.4, 1.6, 1.0, 0.7)

# abcd = (2, 2, 1, -1.01)
# abcd = (2, 1, -0.5, -1.01) # with dt 1.25 makes it go from 1D --> 2D
abcd = (-1.4,1.7,1.0,0.7)
# abcd = (-1.8, -2.0, -0.5, -0.9)
# abcd = (1.6, -0.6, -1.2, 1.6)
# abcd = (-1.7, 1.8, -1.9, -0.4)

def Clifford(xy, abcd):
    x, y = xy
    a, b, c, d = abcd

    dx = np.sin(a * y) + c * np.cos(a * x)
    dy = np.sin(b * x) + d * np.cos(b * y)
    # print(dy)
    return np.array([dx, dy])


dt = 1.35
steps = 1500000

XY = np.empty((steps + 1, 2))
# XY[0] = (0.0, -0.0)
XY[0] = (10.75,8.2)

# apparently the attractor can be written as a jumping style or increment based style 
# aka with or without "XY[i] +"

for i in range(steps):
    XY[i + 1] = XY[i] + Clifford(XY[i], abcd) * dt
    # XY[i + 1] = Clifford(XY[i], abcd) * dt

XY = XY.T

CoM = (np.sum(XY[0, :])/steps, np.sum(XY[1, :]/steps))



print("CoM: ", CoM)




bound = 3





size = 1000

# x = np.round(np.linspace(CoM[0]-bound, CoM[0]+bound, size, dtype=complex), 25)
# y = np.round(np.linspace(CoM[1]+bound, CoM[1]-bound, size, dtype=complex), 25)

x = np.round(np.linspace(8, 12, size, dtype=complex), 25)
y = np.round(np.linspace(10, 6, size, dtype=complex), 25)


X, Y = np.meshgrid(x, y)
Xor, Yor = X, Y

mapp = np.zeros((size, size), dtype=int)

def CliffordGrid(xy, params, count):
    count += 1

    x, y = xy
    a, b, c, d = params

    mask_mapp = (mapp == 0)  # maybe add this mask to the operators

    dx = x + (np.sin(a * y) + c * np.cos(a * x))*dt
    dy = y + (np.sin(b * x) + d * np.cos(b * y))*dt

    mask_1 = (np.sqrt((dx - CoM[0])**2 + (dy - CoM[1])**2) < 1.0)

    mapp[mask_1 & mask_mapp] = count

    return dx, dy, count


counter = 0

for i in range(30):
    X, Y, counter = CliffordGrid((X, Y), abcd, counter)

## just to make axis lines for positive y and positive x axes
mask_Xor = np.logical_and(np.isclose(Xor,0,atol=0.05), Yor > 0)
mask_Yor = np.logical_and(np.isclose(Yor,0,atol=0.05), Xor > 0)
mask_comb = np.logical_or(mask_Xor,mask_Yor)

mapp[mask_comb] = 0

fig2, ax2 = plt.subplots()

plt.imshow(mapp, cmap=plt.cm.twilight_shifted, extent = [8,12,6,10],alpha=1)

# plt.xlim((CoM[0]-bound, CoM[0]+bound))
# plt.ylim((CoM[1]-bound, CoM[1]+bound))

plt.scatter(*XY, s=0.05, alpha=0.2, linewidths=0, color="black")
plt.scatter(CoM[0], CoM[1], s=5, alpha=0.7, linewidths=0, color="cyan")
plt.axis('off')

plt.show()
