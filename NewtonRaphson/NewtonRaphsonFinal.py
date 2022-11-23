import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from mpmath import *
from numpy import *
from sympy import *
 
def iterate(x):
    xn1 = x - ((x**2+1)/(2*x))
    xn1 = simplify(xn1)
    xn1 = xn1.round(2)
    # print(xn1)
    return xn1

def round_complex(x):
    x = complex(x)
    return complex(round(x. real,2),round(x.imag,2))
# https://math.stackexchange.com/questions/2778959/newton-raphson-method-for-complex-numbers
 
r1, r2 = -1*I, 1*I

z = Symbol('z')
y1 = (z**2 + 1)
y2 = diff(y1) #derivative of x**2
 
#plan is to go from -25 to 25 in terms of real plane, -25i to 25i in imaginary plane, step by .1, 500x500 values
arr = zeros((100, 100))
 
# --- PLOTTING --- #
#need this below to index the array, create seperate values for each point and add a counter inside for em
 
for xx in range(100):
    x = -10 + 20 * xx/100
    # if xx % 20 == 0:
    print(f"{xx}/100")
    for yy in range(100):
        y = -10 + 20 * yy/100
       
        if x != 0 or y != 0: # avoid (0,0)
            p = x + y*I
            for i in range(16):
                p = iterate(p)
                
                # if i % 5 == 0:
                    # print(f"{i}/15")
           
            p = round_complex(p)
            # print(p)

            if r1 - p == 0:
                arr[xx][yy] = 1
                # print("I'm 1")
            elif r2 - p == 0:
                arr[xx][yy] = 2
                # print("I'm 2")
    # print(p)

plt.imshow(arr.transpose())
plt.axis('off')
plt.show()
 
 
 
 
