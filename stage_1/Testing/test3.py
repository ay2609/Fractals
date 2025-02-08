import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from mpmath import *
from sympy import *
from sympy.plotting import plot
 
def iterate(x):
#     xn1 = (2/3)*x + (x**2 - y**2)/(3*(x**2 + y**2)**2)
#     yn1 = (2/3)*y - 2*x*y/(3*(x**2 + y**2)**2)
    # xn1 = x - ((x**2 + 1)/(2*x))
    # yn1 = y - ((y**2 + 1)/(2*x))
    xn1 = x - ((x**2+1)/(2*x))
    xn1 = simplify(xn1)
    xn1 = xn1.round(2)
    # print(xn1)
    
    return xn1 ##its not USING Y?? Why isn't it??? how is it supposed to work

def round_complex(x):
    x = complex(x)
    return complex(round(x.real,2),round(x.imag,2))
# https://math.stackexchange.com/questions/2778959/newton-raphson-method-for-complex-numbers
 
r1 = -1*I
r2 = 1*I
 
z = sym.Symbol('z')
y1 = (z**2 + 1)
y2 = sym.diff(y1) #derivative of x**2
 
#plan is to go from -25 to 25 in terms of real plane, -25i to 25i in imaginary plane, step by .1, 500x500 values
arr = np.zeros((100, 100))
 
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
                
                # h = simplify(h - (y1.subs(z,h))/(y2.subs(z,h)))
                # print(p)
                # print(o)
                # p = p - (y1.subs(z,p))/(y2.subs(z,p))
                # o = y1.subs(z,p)
               
                # p = (2/3)*p + (p**2 - o**2)/(3*(p**2 + o**2)**2)
                # o = (2/3)*o - 2*p*o/(3*(p**2 + o**2)**2)
                # print(h)
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
           
            # elif np.round(p, 2) == -0.5 and np.round(o, 2) == -0.87:
                # arr[xx][yy] = 2
            # elif np.round(p, 2) == -0.5 and np.round(o, 2) == 0.87:
            #     arr[xx][yy] = 3
           
           
            # if p.round(2) == 1.0 and o.round(2) == 0:
            #     arr[xx][yy] = 1
            # elif p.round(2) == -0.5 and o.round(2) == -0.87:
            #     arr[xx][yy] = 2
            # elif p.round(2) == -0.5 and o.round(2) == 0.87:
            #     arr[xx][yy] = 3
    # print(p)
 
# equation is like arr[xx][yy]  x + I*y
 
 
#print(yy.shape) # yy has 1000 different values (-5 - 5, 1000) and 4 different lines in it
 
# plt.show()
plt.imshow(arr.transpose())
plt.axis('off')
plt.show()
 
#print(y2.subs(x,2))
 
 
 
 
