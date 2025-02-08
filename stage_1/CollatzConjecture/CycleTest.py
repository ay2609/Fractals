import numpy as np
import math
import time
import gmpy2



start = time.time_ns()


# z = 9999999999

z = 5


rep = 990
print("INIT_Z:",z)

def iterate(z, count: int = 0):

    # Original Equation:

    # if (z%2 == 0):
    #     z = z/2
    # elif (z%2 == 1):
    #     z = 3*z + 1

    # print(z)


    # Equation with Cosine Substitution

    # print("Cosine Boolean",np.cos(math.pi*z))
    # z = ((7*z + 2) - np.cos(math.pi*z)*(5*z+2))/4
    # print(z)


    # Equation with Euler's Equation Substitution

    print("Euler's Equation Boolean",np.round(math.e**(z*math.pi*1j),0))
    z = ((7*z + 2) - np.round(math.e**(z*math.pi*1j),0)*(5*z+2))/4
    print(z)
    




    if abs(z) == 1:
        print("Enters Collatz Cycle")
        return

    if abs(z) > 1000000:
        print("Approaches Infinity")
        return
    
    if count == rep:
        print("Recursion Limit Hit")
        return
    
    return iterate(z,count+1)

iterate(z)

print("-----------\nTime:",(time.time_ns() - start)/10**9)
