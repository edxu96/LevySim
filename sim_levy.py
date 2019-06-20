# setup File for Levy Process
# author: Edward J. Xu
# date: 190620


import numpy as np
import random
import pandas as pd


def cal(a_pre, m_pre, y, phi1, phi2):
    v = random.expovariate(phi1)
    w = random.expovariate(phi2)
    p = a_pre + (v - w)
    a = a_pre + (v - w) + y
    m = max(m_pre, a_pre + v, a)
    return v, w, p, a, m


def sim(n_sample, mu, sigma, lamb, func_sim_dist, vec_para):
    # Calculate phi
    phi1 = mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lamb / sigma ** 2)
    phi2 = - mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lamb / sigma ** 2)
    # Pre-assign lists
    list_v = [0] * n_sample
    list_w = [0] * n_sample
    list_p = [0] * n_sample
    list_a = [0] * n_sample
    list_m = [0] * n_sample
    list_t = [0] * n_sample
    list_y = [0] * n_sample
    list_inter = [0] * n_sample
    # Initialization
    list_y[0] = func_sim_dist(vec_para)
    list_p[0] = 0
    list_a[0] = 0
    list_m[0] = 0
    for i in range(0, n_sample):
        list_inter[i] = random.expovariate(lamb)
        list_t[i] = list_t[i - 1] + list_inter[i]
        list_y[i] = func_sim_dist(vec_para)
        list_v[i], list_w[i], list_p[i], list_a[i], list_m[i] = cal(list_a[i - 1], list_m[i - 1], list_y[i], phi1, phi2)
    datf = pd.DataFrame({
        'v': list_v,
        'w': list_w,
        'y': list_y,
        'p': list_p,
        'a': list_a,
        'm': list_m,
        't': list_t,
        'inter': list_inter
    })
    list_result = [list_p[n_sample - 1], list_a[n_sample - 1], list_m[n_sample - 1]]
    return datf, list_result
