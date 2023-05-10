

#   theory:
# Randomize x many starting points
# Run each point through the attractor equation y many times
#   goal: create an array that ONLY contains values of the actual attractor itself
# compare each point's values to other ones (compounding) to find where the values are all only the attractors
# (if any two values are different)
#   FLAWS
# different points enter the attractor at different times, so comparing the two arrays value by value
# to each other does nothing.

#   theory 2:
# Find for which values of an attractor it starts to loop
# compare to other points

import numpy as np
import matplotlib.pyplot as plt

# also known as the Clifford Attractor

# print(np.round(np.sin(2*math.pi),5))

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

XY = XY.T

CoM = (np.sum(XY[0, :])/steps, np.sum(XY[1, :]/steps))



# SegCoMX = np.empty(6,dtype=float)
# SegCoMY = np.empty(6,dtype=float)

# indStep = np.shape(SegCoMX)[0]

# print(indStep)

# for i in range(0,steps,int(steps/indStep)):
#     print(i)
#     SegCoMX[int(i/(steps/indStep))] = (np.sum(XY[0, i:int(i+(steps/indStep)-1)])/(steps/indStep))
#     SegCoMY[int(i/(steps/indStep))] = (np.sum(XY[1, i:int(i+(steps/indStep)-1)])/(steps/indStep))



print("CoM: ", CoM)
# print("SegCoMX: ", SegCoMX)
# print("SegCoMY: ", SegCoMY)


fig, ax = plt.subplots()

bound = 2

# plt.xlim((CoM[0]-bound, CoM[0]+bound))
# plt.ylim((CoM[1]-bound, CoM[1]+bound))

# plt.xlim((-bound, bound))
# plt.ylim((-bound, bound))

plt.xlim((8,12))
plt.ylim((6,10))

# fig.set_facecolor("black")

plt.scatter(*XY, s=0.05, alpha=0.2, linewidths=0, color="black")
plt.scatter(CoM[0], CoM[1], s=5, alpha=0.7, linewidths=0, color="purple")
# plt.scatter(SegCoMX,SegCoMY,s=5, alpha=0.7, linewidths=0, color="cyan")
plt.axis('off')



size = 500

# x = np.round(np.linspace(-bound, bound, size, dtype=complex), 25)
# y = np.round(np.linspace(bound, -bound, size, dtype=complex), 25)

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

    # mask_1 = any(dx - XY[0,:] < 0.02)

    # print(mask_1)

    mapp[mask_1 & mask_mapp] = count

    return dx, dy, count


counter = 0

for i in range(30):
    X, Y, counter = CliffordGrid((X, Y), abcd, counter)

mask_Xor = np.logical_and(np.isclose(Xor,0,atol=0.05), Yor > 0)
mask_Yor = np.logical_and(np.isclose(Yor,0,atol=0.05), Xor > 0)
mask_comb = np.logical_or(mask_Xor,mask_Yor)

mapp[mask_comb] = 0

fig2, ax2 = plt.subplots()

# ax2.set_xticks(x)
# ax2.set_yticks(y)

# fig2.set_facecolor("black")

# plt.axis('off')

# ax2.invert_yaxis()

plt.imshow(mapp, cmap=plt.cm.twilight_shifted, extent = [8,12,6,10],interpolation='none')

plt.show()
