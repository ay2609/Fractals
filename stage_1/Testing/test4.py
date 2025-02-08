import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from mpmath import *
from sympy import *
from sympy.plotting import plot

# def iterate(x):
#     xn1 = x - ((x**2 + 1)/(2*x))
#     return xn1

def iterate(x):
    xn1 = x - ((y1.subs(z,x))/y2.subs(z,x))
    xn1 = simplify(xn1)
    xn1 = xn1.round(2)
    return xn1

def round_complex(x):
    x = complex(x)
    return complex(round(x.real,2),round(x.imag,2))

# def iterate(x,y):
#     xn1 = x - ((x**2 + 1)/(2*x))
#     yn1 = y - ((y**2 + 1)/(2*y))
#     return xn1, yn1

z = sym.Symbol('z')
y1 = (z**3 - 1)
y2 = sym.diff(y1) #derivative of x**2

r1 = (-0.5 - 0.87*I)
x = -10.00 - 10.00*I
# x = -10.00
# y = -10.00*I
p = x
for i in range(25):
    p = iterate(p)
    print(f"{i}/50")

p = round_complex(p)
if r1 - p == 0:
    print("true")