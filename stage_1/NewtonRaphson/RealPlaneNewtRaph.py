# https://stackoverflow.com/questions/53289609/how-to-graph-points-with-sympy
# https://www.skytowner.com/explore/drawing_the_axis_line_in_matplotlib
# https://stackoverflow.com/questions/44806598/matplotlib-set-color-cycle-versus-set-prop-cycle
# https://matplotlib.org/stable/tutorials/intermediate/color_cycle.html#sphx-glr-tutorials-intermediate-color-cycle-py
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from mpmath import *
from cycler import cycler
from matplotlib.pyplot import axes
from sympy import lambdify, symarray
from sympy.plotting import plot


## 2-3 Hours


# def iterate(x, func):
#     xn1 = 
#     yn1 = 
#     return xn1, yn1


x = sym.Symbol('x')
y1 = (x**2 - 1)
y2 = sym.diff(y1) #derivative of x**2

samplepoint = -3
repeat = 4

arr = symarray('',repeat)

count = 0

    

# --- PLOTTING --- #
fig, (ax) = plt.subplots()
ax.axhline(0) #x - axis line
ax.axvline(0) #y - axis line
xx = np.linspace(-5, 5, 1000)

cy = cycler(color=['black','red','green','cyan'])
ax.set_prop_cycle(cy)

while (count<repeat):
    yfx = y1.subs(x,samplepoint)
    slope = y2.subs(x,samplepoint)
    b = yfx - slope*samplepoint

    y = slope*x+b
    arr[count] = y

    yzero = -b/slope

    plt.plot(yzero, 0 , 'k*') # plot x and y coordinate of desired point
    plt.plot(samplepoint, yfx , 'k*')
    yy = np.transpose(lambdify(x, arr[count])(xx))
    ax.plot(xx, yy)
    samplepoint = yzero
    count = count + 1

print(arr)
yy2 = np.transpose(lambdify(x, [y1])(xx))

ax.plot(xx,yy2)

#print(yy.shape) # yy has 1000 different values (-5 - 5, 1000) and 4 different lines in it

plt.ylim(-10,10)
plt.xlim(-5,5)
plt.show()

#print(y2.subs(x,2))
