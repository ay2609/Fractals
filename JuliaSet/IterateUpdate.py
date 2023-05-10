import numpy as np
import matplotlib.pyplot as plt
import math

# import cv2
# import cmapy
# import PIL

thresh1 = 2
thresh2 = 2.5

gr = (1+np.sqrt(5))/2
a = 15-15j
e = math.e


planex = 1.5 #2*plane by 2*plane spac
planey = 1.5

constplane = 800 #800 is a good value to use for 1kx1k (scale up by whatever you multiply 1k by)
# ^ only applies for roughly square image context






def iterate(z: complex, c: complex, accuracy, precision, step,mapp, ax,size1,size2,count: int =0) -> complex:
    oldsave = mapp

    z = gr*(z**2) + c
    # z = np.round((gr*a)*(((e**(z/a))*(z+1-a))+a-1),20)
    mask2 = (np.absolute(z) > complex(thresh2,thresh2))
    mask3 = (mapp == 0)
    
    if (count < accuracy):
        mapp[mask2 & mask3] = count
    elif (count == accuracy):
        # mapp[mask3] = accuracy
        mapp[mask3] = 0
    
    newsave = mapp
    
    # print(oldsave)
    # print(newsave)

    # print("Redrawing Data")
    plt.clf()
    plt.imshow(mapp,cmap= plt.cm.bone)
    plt.axis('off')
    plt.pause(0.001)
    
    
    if (all(newsave[oldsave == newsave]) == True):
        return


    if count == accuracy:
        print("Completed Drawing")
        return
    

   
    return (iterate(z,c,accuracy, precision, step,mapp,ax,size1,size2,count+1))

def runJulia(size1,size2, accuracy, step, precision, c, mapp):
    fig, ax = plt.subplots()
    plt.imshow(mapp,cmap= plt.cm.magma)
    plt.ion()
    plt.axis('off')
    # print("Drawing Original")
    plt.draw()
    

    # x = np.round(np.linspace(-(size2/constplane), (size2/constplane), size2, dtype=complex), precision)
    # y = np.round(np.linspace(-(size1/constplane)*1j,(size1/constplane)*1j, size1, dtype=complex), precision)
    x = np.round(np.linspace(-(planex), (planex), size2, dtype=complex), precision)
    y = np.round(np.linspace(-(planey)*1j,(planey)*1j, size1, dtype=complex), precision)
    inputs = x + y[:, np.newaxis]

    
    iterate(inputs, c, accuracy, precision, step, mapp, ax,size1,size2)

    plt.show(block=True)



# cmap = plt.cm.magma bone RdBu
# cmap.set_under(0)
# cmap.set_over(accuracy)
# rgba = cmap(145)