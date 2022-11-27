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





#MAKE IT SO THAT YOU HAVE A PICTURE DISPLAYED THAT UPDATES EACH ITERATION

#Change color mapping weight based on distribution of values (i.e. more values within a range means that theyre all mapped to similar colors instead of tons of intricacy) 




size1 = 1000 #y
size2 = 1000 #x
precision = 250
accuracy = 100
mapp = np.zeros((size1, size2),dtype=int)  



# c1 = -0.76 + 0.0838j
# c1 = -0.8 + 0.156j
# c1 = -0.624 + 0.435j
c1 = -0.512511498387847167 + 0.521295573094847167j
# c1 = .716 + .911j
# c1 = -0.222 - .677j
# c1 = -1 + 1j
# if size1 >= 500 and size1 <= 2500 :
#     step =    
#     step = int(step)
# elif size1 < 500:
#     step = 40
# elif size1 > 2500:
#     step = 10

step = int(20000/size2)
# step = 100
# step = 200 
# step = 300
# step = 400 
# step = 500 

# columncount = 1
# for l in range(90,101,10):
#     step = l
#     newstep = 'step {}'.format(step)
#     sheet1.write(0,columncount,newstep)
#     print(newstep)

    
#     newstep = "---------------------------------NEW STEP: {}\n".format(step)
#     with open('data.txt','a') as f:
#                 f.write(newstep)


#     for p in range(0,26,5):
#         if l == 10:
#             sheet1.write(p+1,0,'Trial 1')
#             sheet1.write(p+2,0,'Trial 2')
#             sheet1.write(p+3,0,'Trial 3')
#             sheet1.write(p+4,0,'Trial 4')
#             sheet1.write(p+5,0,'Trial 5')
#         rowcount = 0
#         for m in range(500,2501,500):
#             rowcount+=1
#             start_time = time.time()
#             size1 = m
#             size2 = m
#             mapp = np.zeros((size1, size2), dtype=int)  
#             print("im in trial ", rowcount)
#             print("and my size is ", size1)
#             # index = "-----trial {}-----\nsize: {} \nstep: {} \naccuracy: {} \nprecision: {} \n".format(counting,size,step,accuracy,precision)
#             # with open('data.txt','a') as f:
#             #     f.write(index)
            
            
            
#             runJulia(size1,size2, accuracy, step, precision, c1, mapp)
            
            
#             timer = np.round((time.time() - start_time),2)
#             sheet1.write(p+rowcount,columncount,timer)
#             print(timer)
#             # with open('data.txt','a') as f:
#             #     f.write(timer)
#             wb.save('StepTiming2.xls')
#     columncount+=1
# for t in range(0,5):
#     for m in range(500,2501,500): 
#         start_time = time.time()
#         size1 = m
#         size2 = m
#         mapp = np.zeros((size1, size2), dtype=int)  
#         index = "-----trial-----\nsize: {} \nstep: {} \naccuracy: {} \nprecision: {} \n".format(size1,step,accuracy,precision)
#         print(index)
#         runJulia(size1,size2, accuracy, step, precision, c1, mapp)
#         timer = "--- %s seconds ---\n" % np.round((time.time() - start_time),2)
#         print(timer)
            
    
start_time = time.time()
print("----------\nsize1: {} \nsize2: {} \nplaneconst: {} \nstep: {} \naccuracy: {} \nprecision: {}".format(size1,size2,constplane,step,accuracy,precision))
runJulia(size1,size2, accuracy, step, precision, c1, mapp)
print("--- %s seconds ---" % np.round((time.time() - start_time),2))

plt.show()


 
 
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