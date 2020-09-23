import math
import numpy as np
from numpy.random import seed 
from numpy.random import randint 
from matplotlib import pyplot as plt
import time 
import sys 

def seleccion_ord(A):

    for i in range(len(A)): 
        
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
                
        
        A[i], A[min_idx] = A[min_idx], A[i] 

 
    return A

elements = list() 
times = list() 
data = loadtxt('nombre del archivo')
for i in range(1, 10): 
  
    # generate some integers 
    a = randint(0, 1000 * i, 1000 * i) 
    start = time.time() 
    seleccion_ord(a) 
    end = time.time() 
  
    # print("Sorted list is ", a) 
    print(len(a), "Elementos ordenados por seleccion en ", end-start) 
    elements.append(len(a)) 
    times.append(end-start) 
  

plt.xlabel('Longitud de la lista') 
plt.ylabel('Tiempo de ejecución') 
plt.plot(elements, times, label ='Selección Sort') 
plt.grid() 
plt.legend() 
plt.show() 




