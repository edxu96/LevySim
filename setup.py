# setup File for Levy Process
# author: Edward J. Xu

import numpy as np
import scipy.stats as stats
import random
import matplotlib.pyplot as plt


def sim_levy(t, mu, sigma, aPre):
    phi1 = mu / sigma^2 + np.sqrt(mu^2 / sigma^4 + 2 * lambda / sigma ^ 2)
    phi2 = - mu / sigma^2 + np.sqrt(mu^2 / sigma^4 + 2 * lambda / sigma ^ 2)
    v = random.expovariate(phi1)
    w = random.expovariate(phi2)
    p = aPre + (v - w)
    a = aPre + (v - w) + y
    return v, w, x


def sim_v(num_v):
    list_v = [0] * num_v
    for i in range(0, num_v):
        t = random.expovariate(1 / lambda)
        list_v[i] =



def sim_w()


def test():
    mu = 0
    sigma = 0
    lambda = 0
    nSim = 100
    phi1 = mu / sigma^2 + sqrt(mu^2 / sigma^4 + 2 * lambda / sigma^2)
    phi2 = - mu / sigma^2 + sqrt(mu^2 / sigma^4 + 2 * lambda / sigma^2)



    for i in range(0, nSim):
        tInter = random.exp(lambda)
        sim_levy(t, mu, sigma)



test()