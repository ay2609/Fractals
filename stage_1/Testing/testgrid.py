import matplotlib.pyplot as plt
import numpy as np
import pygnuplot 
import h5py
import pandas as pd

x = np.round(np.linspace(-5,5,1000,dtype=complex),3)
y = np.round(np.linspace(5j,5j,1000,dtype=complex),3)

mapp = np.zeros((5,5),dtype=int)

c = 10

inputs = x + y[:, np.newaxis]

p = np.split(inputs, 2)
print(p)

# list(f.keys())
# print(x,y)

# print(dset)