# setup File for Levy Process
# author: Edward J. Xu
# date: 190620


import numpy as np
# import scipy.stats as stats
import random
# import matplotlib.pyplot as plt


def cal(mu, sigma, a_pre, m_pre, y, lamb):
    phi1 = mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lamb / sigma ** 2)
    phi2 = - mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lamb / sigma ** 2)
    v = random.expovariate(phi1)
    w = random.expovariate(phi2)
    p = a_pre + (v - w)
    a = a_pre + (v - w) + y
    m = max(m_pre, a_pre + v, a_pre + (v - w) + y)
    return v, w, p, a, m


def sim(num_sim, mu, sigma, lamb, lamb_y):
    # initialize
    list_v = [0] * num_sim
    list_w = [0] * num_sim
    list_p = [0] * num_sim
    list_a = [0] * num_sim
    list_m = [0] * num_sim
    list_t = [0] * num_sim
    list_y = [0] * num_sim
    list_inter = [0] * num_sim
    #
    list_y[0] = random.expovariate(lamb_y)
    list_p[0] = 0
    list_a[0] = 0
    list_m[0] = 0
    for i in range(0, num_sim):
        list_inter[i] = random.expovariate(lamb)
        list_t[i] = list_t[i - 1] + list_inter[i]
        list_y[i] = random.expovariate(1)
        list_v[i], list_w[i], list_p[i], list_a[i], list_m[i] = cal_levy(mu, sigma, list_a[i - 1], list_m[i - 1],
                                                                         list_y[i], lamb)
    return list_p[num_sim - 1], list_a[num_sim - 1], list_m[num_sim - 1]
