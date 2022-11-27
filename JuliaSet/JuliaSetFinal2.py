import matplotlib.pyplot as plt
import numpy as np
import time
from IterateUpdate import *
import warnings

from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

warnings.filterwarnings("ignore")
# with open('data.txt','w') as f:
#     f.write("\n")





#MAKE IT SO THAT YOU HAVE A PICTURE DISPLAYED THAT UPDATES EACH ITERATION (done)

#Change color mapping weight based on distribution of values (i.e. more values within a range means that theyre all mapped to similar colors instead of tons of intricacy) 

#COUNT AMOUNT OF VALUES ESCAPED PER ITERATION AND MAKE A LINE GRAPH!!!
#COUNT AMOUNT OF VALUES ESCAPED PER ITERATION AND MAKE A LINE GRAPH!!!
#COUNT AMOUNT OF VALUES ESCAPED PER ITERATION AND MAKE A LINE GRAPH!!!
#COUNT AMOUNT OF VALUES ESCAPED PER ITERATION AND MAKE A LINE GRAPH!!!


size1 = 1000 #y
size2 = 1000 #x
precision = 100
accuracy = 200
mapp = np.zeros((size1, size2), dtype=int)  



# c1 = -0.76 + 0.0838j
# c1 = -0.8 + 0.156j
# c1 = -0.624 + 0.435j
# c1 = .28 + 0.008j #good one
c1 = -0.512511498387847167 + 0.521295573094847167j
# c1 = .716 + .911j
# c1 = -0.222 - .677j
# c1 = -1 + 1j


step = int(20000/size2)

# start_time = time.time()
print("----------\nsize1: {} \nsize2: {} \nplaneconst: {} \nstep: {} \naccuracy: {} \nprecision: {}".format(size1,size2,constplane,step,accuracy,precision))
runJulia(size1,size2, accuracy, step, precision, c1, mapp)
# print("--- %s seconds ---" % np.round((time.time() - start_time),2))

# plt.show()


 
 
###MAKE ANOTHER MATRIX FULL OF Y VALUES AND GRAPH THAT TOO, 3 D FUNCTIONS!!!!
### Graph Riemann Sum vector field
# https://www.youtube.com/watch?v=sD0NjbwqlYw
#steiner chain orbit trap
#steiner chain
 
# plt.imshow(map,cmap = plt.cm.twilight_r)
# plt.imshow(map,cmap= plt.cm.twilight_shifted)
# plt.imshow(map,cmap= plt.cm.cividis)
# plt.imshow(map,cmap= plt.cm.inferno)
# plt.imshow(map,cmap= plt.cm.rainbow)