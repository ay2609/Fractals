import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def Thomas(xyz, b):
    x, y, z = xyz

    dx = np.sin(y) - b * x
    dy = np.sin(z) - b * y
    dz = np.sin(x) - b * z

    return np.array([dx, dy, dz])


b = 0.208186

dt = 0.01
steps = 35000

XYZ = np.empty((steps + 1, 3))

fig = plt.figure()

ax = fig.add_subplot(projection='3d')

XYZ[0] = (-0.33, -0.1, -0.25)

for i in range(steps):
    XYZ[i+1] = XYZ[i] + Thomas(XYZ[i], b) * dt


def animate(i):
    ax.clear()

    ax.plot(*XYZ[0:i].T, color='cyan', ms=0.1)


ax.set_facecolor('black')
ax.axis('off')
ax.set_title("TCSA Attractor")
# ax.set_xlim([-1.5, 1.5])
# ax.set_ylim([-1.5, 1.5])
# ax.set_zlim([-1.5, 1.5])


ani = FuncAnimation(fig=fig,
                    func=animate,
                    interval=1,
                    frames=range(0, steps, 25)
                    # blit=True,
                    # repeat=True,
                    )
# ax.plot(*XYZ[0:i].T, color='cyan', ms=0.1)

plt.show()
