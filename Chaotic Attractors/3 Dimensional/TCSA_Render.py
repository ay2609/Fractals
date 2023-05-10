## Thomas' Cyclically Symmetric Attractor
import numpy as np
import matplotlib.pyplot as plt
import cmath

def Thomas(xyz, b, i):
    x, y, z = xyz
    
    dx = np.sin(y) - b*x
    dy = np.sin(z) - b*y
    dz = np.sin(x) - b*z

    XYZvelo[i] = np.sqrt((dx**2) + (dy**2) + (dz**2))

    return np.array([dx,dy,dz])

# b = 1
b = 0.208186
# b= 0.1998
# b = 0.32899
dt = 0.01
steps = 35000

XYZvelo = np.empty((steps+1))

XYZ = np.empty((steps+1,3))
XYZ[0] = (-0.33,-0.1,-0.25)
# XYZ[0] = (0.33,0.1,0.25)
for i in range(steps):
    XYZ[i+1] = XYZ[i] + Thomas(XYZ[i],b, i) * dt

XYZvelo = XYZvelo/max(XYZvelo)
XYZvelo = np.round(XYZvelo,3)

XYZ = XYZ.T



fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))


"""
Notes--
For a b value of 0.208186, no matter the starting point, the system always falls back into the same exact orbit.
I think in this case, the attractor itself is the orbit the point falls into. The wiki describes it as having become chaotic.

There are TWO attractors, which are symmetrical to eachother (in every regard?).

"""
colors = plt.cm.twilight_shifted(XYZvelo)

XYZ = XYZ.T

ax.scatter(*XYZ,color=colors,s=0.01)
ax.set_facecolor('black')


ax.axis('off')

ax.set_title("Thomas' Cyclically Symmetric Attractor")

plt.show()



# Initial code by pm5k, thanks!
import array

image_width  = 100
image_height = 100

# Make a 3-component (RGB) image (array of pixels) of resolution image_height x image_width.
pixels = array.array('B', [0] * image_width * image_height * 3)

for y in range(0, image_height):
    for x in range(0, image_width):
        # Compute the array index for a given (x, y) coordinate and image width.
        pixel_index = y * image_width + x

        # For each pixel, there are 3 bytes: one for red, green and blue.
        # So for each pixel_index, we multply by 3 and add offsets of 0, 1, 2 for the RGB components.
        pixels[pixel_index * 3 + 0] = 128  # Red
        pixels[pixel_index * 3 + 1] = 234 # Green
        pixels[pixel_index * 3 + 2] = 29 # Blue

# PPM image format header. See https://en.wikipedia.org/wiki/Netpbm
ppm_maxval = 255
ppm_header = f"P6 {image_width} {image_height} {ppm_maxval}\n"

# Save the image in PPM format as a binary file.
ppm_bytes = bytearray(ppm_header, 'ascii')
with open("out.ppm", "wb") as f:
    f.write(ppm_bytes)
    pixels.tofile(f)