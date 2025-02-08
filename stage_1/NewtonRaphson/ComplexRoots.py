# Complex Roots
# Nathan Rabinovitch
# 10/25/22 m/d/y

import numpy as np
import matplotlib.pyplot as plt
#from PIL import Image as im
    
def iterate(x, y):
    xn1 = (2/3)*x + (x**2 - y**2)/(3*(x**2 + y**2)**2)
    yn1 = (2/3)*y - 2*x*y/(3*(x**2 + y**2)**2)
    # print(xn1)
    # print(yn1)
    return xn1, yn1
            
##x = -0.5
##y = 3**0.5 / 2
##
##a = 50
##x *= a
##y *= a
##for j in range(40):
##    x, y = iterate(x, y)
##print(x, y)

# 1,    0   maps to 1
# -0.5, -0.866 maps to 2
# -0.5,  0.866 maps to 3

arr = np.zeros((500, 500))

for n in range(500):
    x = -10 + 20 * n/500
    if n % 20 == 0:
        print(f"{n}/500")
    for m in range(500):
        y = -10 + 20 * m/500
        # print(x)
        # print(y)
        if x != 0 or y != 0: # avoid (0,0)
            p, o = iterate(x,y)
            for i in range(50):
                p, o = iterate(p, o)

            if np.round(p, 2) == 1.0 and np.round(o, 2) == 0:
                arr[n][m] = 1
            elif np.round(p, 2) == -0.5 and np.round(o, 2) == -0.87:
                arr[n][m] = 2
            elif np.round(p, 2) == -0.5 and np.round(o, 2) == 0.87:
                arr[n][m] = 3

#294 357
#369 421

##for n in range(294, 369):
##    x = -10 + 20 * n/500
##    if n % 20 == 0:
##        print(f"{n}/500")
##    for m in range(357, 421):
##        y = -10 + 20 * m/500
##
##        if x != 0 or y != 0:
##            p, o = iterate(x,y)
##            for i in range(50):
##                p, o = iterate(p, o)
##
##            if np.round(p, 2) == 1.0 and np.round(o, 2) == 0:
##                arr[n][m] = 1
##            elif np.round(p, 2) == -0.5 and np.round(o, 2) == -0.87:
##                arr[n][m] = 2
##            elif np.round(p, 2) == -0.5 and np.round(o, 2) == 0.87:
##                arr[n][m] = 3

plt.imshow(arr.transpose())
plt.axis('off')
##plt.xlim(294, 369)
##plt.ylim(357, 421)
plt.show()
