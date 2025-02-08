# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# # Create a figure and set the limits of the x and y axes
# fig = plt.figure()
# ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

# # Create a line that will be animated
# line, = ax.plot([], [], lw=2)

# # This function will be called for each frame of the animation
# def animate(i):
#     # Calculate the points on the complex plane
#     points = []
#     x = y = -2
#     while x <= 2:
#         while y <= 2:
#             # Use the Mandelbrot set equation to calculate the next point
#             c = complex(x, y)
#             z = 0
#             for j in range(i):
#                 z = z**2 + c
#             # If the point is in the set, add it to the list of points
#             if abs(z) <= 2:
#                 points.append([x, y])
#             y += 0.05
#         x += 0.05
#         y = -2

#     # Update the line with the new points
#     line.set_data(array(points).T)

# # Create the animation
# anim = animation.FuncAnimation(fig, animate, frames=50, interval=20)

# # Show the animation
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import complex, array

# Create a figure and set the limits of the x and y axes
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

# This function will be called for each frame of the animation
def animate(i):
    # Calculate the points on the complex plane
    points = []
    x = y = -2
    while x <= 2:
        while y <= 2:
            # Use the Mandelbrot set equation to calculate the next point
            c = complex(x, y)
            z = 0
            for j in range(i):
                z = z**2 + c
            # If the point is in the set, add it to the list of points
            if abs(z) <= 2:
                points.append([x, y])
            y += 0.05
        x += 0.05
        y = -2

    # Use the scatter() method to plot the points with a colormap
    ax.scatter(array(points).T[0], array(points).T[1], c=array(points).T[0], cmap='viridis')

# Create the animation
anim = animation.FuncAnimation(fig, animate, frames=50, interval=20)

# Show the animation
plt.show()
