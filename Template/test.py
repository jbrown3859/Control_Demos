import numpy as np
from scipy import io, integrate, linalg, signal
from scipy.sparse.linalg import eigs
import control
import slycot

np.set_printoptions(precision=3,suppress=True)

arr = np.arange(9).reshape(3,3)
print("Array = \n",arr,"\n")


D,V = eigs(arr)
print("Eigs : ", D, "\n")
print("EigVs : \n", V, "\n")