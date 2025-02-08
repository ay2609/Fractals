import copy
import numpy as np
import matplotlib.pyplot as plt

abcd = (-1.4, 1.7, 1.0, 0.7)


def clifford_boundary(max_iterations, a=-1.4, b=1.7, c=1.0, d=0.7):
    ''' A function to map the boundaries of attraction of the
    Clifford system, iterated semicontinuously. Takes a number of
    maximum iterations and Clifford constants as inputs, outputs
    a color-coded map of which values end up in a given basin of
    attraction over time.
    '''

    x_range = 1500
    y_range = 1500

    x_list = np.arange(8, 12, 4 / x_range)
    y_list = np.arange(10, 6, -4 / y_range)
    array = np.meshgrid(x_list, y_list)
    print(np.shape(array))

    x2 = np.zeros(x_range)
    y2 = np.zeros(y_range)
    iterations_until_in_basin = np.meshgrid(x2, y2)
    for i in iterations_until_in_basin:
        for j in i:
            j += max_iterations

    not_already_in_basin = iterations_until_in_basin[0] < 10000

    for k in range(max_iterations):
        array_copied = copy.deepcopy(array[0])  # copy array to prevent premature modification of x array

        # clifford map applied to array
        array[0] = array[0] + 1.35 * (np.sin(a * array[1]) + c * np.cos(a * array[0]))
        array[1] = array[1] + 1.35 * (np.sin(b * array_copied) + d * np.cos(b * array[1]))

        # note which array elements are enter the basin of attraction
        in_basin = np.abs(array[0] - 10.95) + np.abs(array[1] - 8.1) < 1
        entering_basin = in_basin & not_already_in_basin
        iterations_until_in_basin[0][entering_basin] = k
        not_already_in_basin = np.invert(entering_basin) & not_already_in_basin

    return iterations_until_in_basin[0]


def clifford(xy, abcd):
    x, y = xy
    a, b, c, d = abcd

    dx = (np.sin(a * y) + c * np.cos(a * x)) * dt
    dy = (np.sin(b * x) + d * np.cos(b * y)) * dt
    # print(dy)
    return np.array([dx, dy])


dt = 1.35
steps = 150000

XY = np.empty((steps + 1, 2))
XY[0] = (10.75, 8.2)

for i in range(steps):
    XY[i + 1] = XY[i] + clifford(XY[i], abcd)

XY = XY.T

fig, ax = plt.subplots()
plt.imshow(clifford_boundary(30), extent=[8, 12, 6, 10], cmap='twilight_shifted', alpha=1, interpolation='none')
plt.scatter(XY[0, :], XY[1, :], color="white", alpha=0.6, s=0.05, lw=0)
ax.axis('off')
fig.set_facecolor("black")
plt.savefig('CLIFFORD_BOUNDARY', dpi=1000, bbox_inches='tight', pad_inches=0)
plt.show()
# plt.close()
