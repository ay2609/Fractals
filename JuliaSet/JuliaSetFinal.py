import matplotlib.pyplot as plt
import numpy as np
import time
from Iterate import *
import warnings

from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

warnings.filterwarnings("ignore")
# with open('data.txt','w') as f:
#     f.write("\n")



size1 = 500 #y
size2 = 500 #x
precision = 250
accuracy = 500

# c1 = -0.76 + 0.0838j
c1 = -0.8 + 0.156j
step = 15
# step = 200 
# step = 300
# step = 400 
# step = 500 

columncount = 1
for l in range(10,101,10):
    step = l
    newstep = 'step {}'.format(step)
    sheet1.write(0,columncount,newstep)
    print(newstep)

    
    # newstep = "---------------------------------NEW STEP: {}\n".format(step)
    # with open('data.txt','a') as f:
    #             f.write(newstep)


    for p in range(0,16,5):
        if l == 10:
            sheet1.write(p+1,0,'Trial 1')
            sheet1.write(p+2,0,'Trial 2')
            sheet1.write(p+3,0,'Trial 3')
            sheet1.write(p+4,0,'Trial 4')
            sheet1.write(p+5,0,'Trial 5')
        rowcount = 0
        for m in range(500,2501,500):
            rowcount+=1
            start_time = time.time()
            size1 = m
            size2 = m
            mapp = np.zeros((size1, size2), dtype=int)  
            print("im in trial ", rowcount)
            print("and my size is ", size1)
            # index = "-----trial {}-----\nsize: {} \nstep: {} \naccuracy: {} \nprecision: {} \n".format(counting,size,step,accuracy,precision)
            # with open('data.txt','a') as f:
            #     f.write(index)
            
            
            
            runJulia(size1,size2, accuracy, step, precision, c1, mapp)
            
            

            timer = np.round((time.time() - start_time),2)
            sheet1.write(p+rowcount,columncount,timer)
            print(timer)
            # with open('data.txt','a') as f:
            #     f.write(timer)
            wb.save('StepTiming.xls')
    columncount+=1

# for m in range(2000,2001,1000): 
#     start_time = time.time()
#     size = m
#     index = "-----trial-----\nsize: {} \nstep: {} \naccuracy: {} \nprecision: {} \n".format(size,step,accuracy,precision)
#     print(index)
#     runJulia(size, accuracy, step, precision, c1)
#     timer = "--- %s seconds ---\n" % np.round((time.time() - start_time),2)
#     print(timer)
            
    
# start_time = time.time()
# print("----------\nsize1: {} \nsize2: {} \nplaneconst: {} \nstep: {} \naccuracy: {} \nprecision: {}".format(size1,size2,constplane,step,accuracy,precision))
# runJulia(size1,size2, accuracy, step, precision, c1, mapp)
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