import matplotlib.pyplot as plt
import numpy as np

x:complex = -10 - 10.01j

if np.absolute(x.real) >= 10 or np.absolute(np.round(x.imag,0)) >= 10j:
    print("true")
else:
    print("false")

print(np.round(x,2))