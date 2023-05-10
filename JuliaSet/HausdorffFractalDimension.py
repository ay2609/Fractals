import numpy as np
import matplotlib.pyplot as plt
from Iterate import PLANE_X


mapp = np.load('mapp.npy') # load in the array
SHAPE_X = np.shape(mapp)[0] # attain the length of the array
DeltaVAL = PLANE_X*2 # initialize the first division increment (useless btw)

# print(np.round(12.2 % 1,2))

# Calculate the amount of times you can make new amounts of boxes before your box increment becomes non-integer
def N_CALC(X_SHAPE:int) -> int:
    count = 0
    len = X_SHAPE
    while(True):
        if len % 2 == 0:
            count += 1
            len /= 2

        elif len % 2 != 0:
            return count

print("SHAPE_X", SHAPE_X)
print("PLANE_X", PLANE_X)


n = N_CALC(SHAPE_X)
n = n
DeltaArray = np.zeros(n,dtype=float)
XArray = np.zeros(n,dtype=int)

for m in range(0,n):
    DELTA = SHAPE_X/(2**m)
    DeltaVAL = (PLANE_X*2)/(2**m)
    DeltaArray[m] = DeltaVAL
    print("DELTA:",DELTA)
    print("DeltaVAL:",DeltaVAL)
    print("DeltaARR:",DeltaArray)
    loop = SHAPE_X/(SHAPE_X/(2**m))
    boxamount = loop**2
    print("loop:", loop)
    print("boxes:",boxamount)
    print("boxsize:",DELTA**2)
    
    # print("boxsize:",DeltaVAL**2)

    # Hausdorff Method Box Tracking
    for i in range(0,SHAPE_X,int(DELTA)):
        # print("i:",i)
        for j in range(0,SHAPE_X,int(DELTA)):
            # print("j:",j)
            if (((mapp[i:i+int(DELTA)-1,j:j+int(DELTA)-1])==1).any()):
                XArray[m] = XArray[m]+1
            
    print("XARR:",XArray)
    print("-------------")

DeltaArray = -np.log(DeltaArray)
XArray = np.log(XArray)


# plt.style.use('seaborn-whitegrid')
# plt.plot(DeltaArray[1::],XArray[1::],'o',color='black')
plt.plot(DeltaArray[0::],XArray[0::],'o',color='black')

# a, b = np.polyfit(DeltaArray[1::],XArray[1::],1)
a2, b2 = np.polyfit(DeltaArray,XArray,1)

# plt.plot(DeltaArray[1::],a*DeltaArray[1::]+b)
plt.plot(DeltaArray[0::],a2*DeltaArray[0::]+b2)

print("Coeffecient: ",(a2))
print("ln C / Shift:", b2)

# plt.show()
# 0.999023438


# print(n)




# np.log()









fig, ax = plt.subplots()
plt.imshow(mapp,cmap=plt.cm.bone)
plt.axis('off')
ax.invert_yaxis()
plt.show()