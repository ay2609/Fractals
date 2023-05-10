import numpy as np
import time

# <2 Hours

# Variables

X,Y = (-0.25,+.15)

C = -0.25 + .15j

Z = 0

Rep = 10000000

start_time = time.time()

for i in range(Rep):
    # Z = Z*Z + C
    Xnew = X*X + Y*Y + X
    Y = 2*X*Y + Y
    X = Xnew
    
print(X,Y)

print("--- %s seconds ---" % np.round((time.time() - start_time),10))