import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives

state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 100.0 , .01)

states = odeint(f, state0, t)

print(states[:,0])
print(states[:,2])
fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
ax = fig.add_subplot()
# ax.plot(states[:, 0], states[:, 1], states[:, 2])
ax.plot(states[:, 0], states[:, 2])
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
# ax.set_zlabel("Z Axis")
plt.draw()
plt.show()