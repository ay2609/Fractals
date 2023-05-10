import numpy as np
import matplotlib.pyplot as plt

# known as the Clifford Boundary

abcd = (-1.4,1.7,1.0,0.7)

dt = 1.35
size = 1000

x = np.linspace(8, 12, size, dtype=complex)
y = np.linspace(10, 6, size, dtype=complex)


X, Y = np.meshgrid(x, y)

mapp = np.zeros((size, size), dtype=int)

def CliffordGrid(xy, params, count):
    count += 1

    x, y = xy
    a, b, c, d = params

    mask_mapp = (mapp == 0)  # maybe add this mask to the operators

    dx = x + (np.sin(a * y) + c * np.cos(a * x))*dt
    dy = y + (np.sin(b * x) + d * np.cos(b * y))*dt

    mask_1 = (np.sqrt((dx - (10.931058924787669))**2 + (dy - (8.074184029806359))**2) < 1)
    # mask_1 = np.abs(dx - 10.931) + np.abs(dy - 8.074) < 1
    
    mapp[mask_1 & mask_mapp] = count

    return dx, dy, count


counter = 0

for i in range(30):
    X, Y, counter = CliffordGrid((X, Y), abcd, counter)



fig2, ax2 = plt.subplots()

plt.imshow(mapp, cmap=plt.cm.twilight_shifted, extent = [8,12,6,10], alpha=1)

plt.show()
