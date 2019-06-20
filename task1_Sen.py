# task 1

from random import random
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy.random as npr
import math

nLoop = 1
jump = 1000

lambda1 = 1
mu = 0.5
sigma = 1
phi1 = mu/(sigma**2) + math.sqrt(mu**2/sigma**4+2*lambda1/sigma**2)
phi2 = -mu/(sigma**2) + math.sqrt(mu**2/sigma**4+2*lambda1/sigma**2)

A1k = [0] * nLoop
M1k = [0] * nLoop
P1k = [0] * nLoop   

for ind in range(1,nLoop+1):
    T = [0] * (jump+1)
    A = [0] * (jump+1)
    M = [0] * (jump+1)
    P = [0] * (jump+1) 
    V = [0] * (jump+1)
    W = [0] * (jump+1)    
    Y = [0] * (jump+1)    
    for j in range(1, jump+1):
        T[j] = T[j-1] + npr.exponential(lambda1)
        V[j] = npr.exponential(phi1)
        W[j] = npr.exponential(phi2)
        P[j] = A[j-1] + V[j] - W[j]
        Y[j] = npr.exponential(1)
        A[j] = P[j] + Y[j]
        M[j] = max(M[j-1], A[j-1]+V[j], A[j])
        
    A1k[ind-1] = A[jump]
    P1k[ind-1] = P[jump]
    M1k[ind-1] = M[jump]
    
    plt.plot(T, A)
    #plt.plot(T, [V[i]-W[i] for i in range(jump+1)])
    plt.show()
  

        
        
        
        
        
        
        