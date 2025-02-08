import numpy as np
import matplotlib.pyplot as plt
import os
import cmasher as cmr

# ToDo, Things to experiment with: Changing size of basin of attraction, changing iter count, figure out overflow errors.


def lorenz(xyz, *, s=10, r=28, b=2.667):
    x, y, z = xyz
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return np.array([x_dot, y_dot, z_dot])


def lorenz_grid(xyz, count, s=10, r=28, b=2.667):
    x, y, z = xyz

    mask = (mapp == 0)
    alt_mask = (alt_mapp == 0)

    dist = np.sqrt((x - averages[0]) ** 2 + (z - averages[1]) ** 2)
    mask_1 = dist < min_radius
    mask_2 = dist > max_radius

    mapp[mask_1 & mask] = count
    alt_mapp[mask_2 & alt_mask] = count

    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z

    x_dot[mask_1 | mask_2] = 0
    y_dot[mask_1 | mask_2] = 0
    z_dot[mask_1 | mask_2] = 0

    return np.array([x_dot, y_dot, z_dot])


dt = 0.01
num_steps = 100000

xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (0., 1., 8.)  # Set initial values
# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

averages = np.average(xyzs[:, [0, 2]].T, axis=1)  # the CoM
max_dist = max(xyzs[:, [0, 2]], key=lambda x: np.sqrt((x[0] - averages[0]) ** 2 + (x[1] - averages[1]) ** 2))
min_radius = np.sqrt((max_dist[0] - averages[0]) ** 2 + (max_dist[1] - averages[1]) ** 2)
max_radius = 1e3

bounds = 125
center = averages
# center = [71., 71.]
# center = [0., -41.] # on 1/1.75 radius, makes a heart

xlb, xub = center[0] - bounds, center[0] + bounds
zlb, zub = center[1] - bounds, center[1] + bounds

# MAKING FRACTAL --

size = 500

x = np.round(np.linspace(xlb, xub, size, dtype=complex), 25)
z = np.round(np.linspace(zub, zlb, size, dtype=complex), 25)

X, Z = np.meshgrid(x, z)
Y = np.zeros_like(X)
mapp = np.zeros((size, size), dtype=int)  # so we only edit values that haven't already been changed
alt_mapp = np.zeros_like(mapp)

counter = 0
for i in range(150):
    counter += 1
    X, Y, Z = (X, Y, Z) + lorenz_grid((X, Y, Z), counter) * dt

# PLOTTING --

plt.figure(figsize=(8, 6), facecolor='#000000')

plt.imshow((mapp / np.max(mapp)) ** (1 / 3.2), cmap=plt.cm.twilight_shifted, extent=[xlb, xub, zlb, zub], alpha=1, interpolation='none')
# plt.imshow(mapp, cmap=plt.cm.twilight_shifted, extent=[xlb, xub, zlb, zub], alpha=1, interpolation='none')


overlay_alt_mapp = np.ma.masked_array(alt_mapp, alt_mapp == 0)
plt.imshow((overlay_alt_mapp / np.max(overlay_alt_mapp)) ** (1 / 2), cmap='cmr.gothic', extent=[xlb, xub, zlb, zub], alpha=0.75, interpolation='none')
# plt.imshow(overlay_alt_mapp, cmap='cmr.gothic', extent=[xlb, xub, zlb, zub], alpha=0.75, interpolation='none')


plt.axis('off')

plt.plot(*xyzs[0:20000, [0, 2]].T, lw=0.05, color="black", alpha=0.5)

plt.xlim(xlb, xub)
plt.ylim(zlb, zub)

# ax.scatter(*averages, s=25, color='r', zorder=3)
# ax.set_title("Lorenz Attractor")

counter = 1
while os.path.exists(f"lorenz/plot_{counter}.png"):
    counter += 1

# Save the plot
filename = f"lorenz/plot_{counter}.png"
plt.savefig(filename, dpi=500, bbox_inches='tight', pad_inches=0)
plt.show()
