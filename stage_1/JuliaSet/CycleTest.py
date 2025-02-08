import numpy as np
import cmath
import time
import gmpy2



start = time.time_ns()


# z = 9999999999

z = .5487348075284752385j + .323042738


rep = 990
print("INIT_Z:",z)

def iterate(z, count: int = 0):
    # z = 1/(z**2)
    # z = (z**2)
    # z = int((z**2)/10000000000)
    zp = z
    z = (z**2)
    zp = gmpy2.mul(zp,zp)

    print("diff:", abs(gmpy2.sub(zp,z)))

    # if np.round(abs(z)) % 2 == 1:
    #     z = 3*z + 1
    # else:
    #     z /= 2
    



    # print("COUNT:",count," Z:",z)

    # if np.round(z,2) == 1:
    #     return


    if abs(z) < 0.00000001:
        print("Approaches 0")
        return

    # if abs(z) > 100000000:
    #     print("Approaches Infinity")
    #     return
    
    if count == rep:
        print("Recursion Limit Hit")
        return
    
    return iterate(z,count+1)

iterate(z)

print((time.time_ns() - start)/10**9)
