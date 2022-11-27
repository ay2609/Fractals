import numpy as np
import matplotlib.pyplot as plt
# import pygame
 #250 for testing time  
thresh1 = 3
thresh2 = 6


#for 4k size
# step = 250 # 149.65 sec # 15.2 sec for 1k
# step = 100 # 193.76 sec # 10.63 sec
# step = 400 # 169.76 sec # 11.3 sec
# step = 500 # not even worth trying # 16.44
# step = 200 # 155.4 sec




planex = 1.25 #2*plane by 2*plane spac
planey = 1.25

constplane = 800 #800 is a good value to use for 1kx1k (scale up by whatever you multiply 1k by)






def iterate(z: complex, c: complex, i, accuracy, precision, step,mapp, count: int =0) -> complex:
    oldsave = mapp[i:i+step,:]
    #boolean index this thing below for every value that does not equal -1
    # mask = (z < complex(thresh2,thresh2))
    # z[mask] = z[mask]**2 + c
    # np.putmask(z,mask, z**2 + c)

    z = z**2 + c


    # zf = z**5 + c
    # zf = np.round((z - ((z**3-c)/(3*(z**2)))),precision)
    # print(zf)

    mask2 = (np.absolute(z) > complex(thresh2,thresh2))
    mask3 = (mapp[i:i+step,:] == 0)
    
    if (count < accuracy):
        mapp[i:i+step,:][mask2 & mask3] = count
    elif (count == accuracy):
        mapp[i:i+step,:][mask3] = accuracy
    # mapp[i,:][np.absolute(z) > complex(thresh2,thresh2)] = count
    newsave = mapp[i:i+step,:]
    
    
    if (all(newsave[oldsave == newsave]) == True):
        return


    if count == accuracy:
        return

   
    return (iterate(z,c,i,accuracy, precision, step,mapp,count+1))

def runJulia(size1,size2, accuracy, step, precision, c, mapp):
    
    
    # counter = 0
    # totalprogress= (size/step)**2
    # print(np.round((counter/totalprogress)*100,2),"%")
    
    

    # x = np.round(np.linspace(-(size2/constplane), (size2/constplane), size2, dtype=complex), precision)
    # y = np.round(np.linspace(-(size1/constplane)*1j,(size1/constplane)*1j, size1, dtype=complex), precision)
    x = np.round(np.linspace(-(planex), (planex), size2, dtype=complex), precision)
    y = np.round(np.linspace(-(planey)*1j,(planey)*1j, size1, dtype=complex), precision)
    inputs = x + y[:, np.newaxis]

    for i in range(0,size1,step):
        iterate(inputs[i:i+step,:], c, i, accuracy, precision, step, mapp)
        # print("------inside iter----\nsize: {} \nstep: {} \naccuracy: {} \nprecision: {}".format(size,step,accuracy,precision))
        # counter = counter +1 
        # print(np.round((counter/totalprogress)*100,1),"%")
    fig, ax = plt.subplots()
    plt.imshow(mapp,cmap= plt.cm.magma)
    ax.invert_yaxis()   
    plt.axis('off')

# cmap = plt.cm.magma bone RdBu
# cmap.set_under(0)
# cmap.set_over(accuracy)
# rgba = cmap(145)