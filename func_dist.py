# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import numpy as np
import scipy.stats as st

def exp(lamb):
    return np.random.exponential(1/lamb, size = 1)

# rvs(a, loc=0, scale=1, size=1, random_state=None)
    
def erlang(shape):
    return st.erlang(shape).rvs()


