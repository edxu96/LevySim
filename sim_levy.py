# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import random
import pandas as pd


def cal(a_pre, m_pre, y, phi1, phi2):
    v = random.expovariate(1 / phi1)
    w = random.expovariate(1 / phi2)
    p = a_pre + (v - w)
    a = a_pre + (v - w) + y
    m = max(m_pre, a_pre + v, a)
    return v, w, p, a, m


def sim(n_sample, phi1, phi2, lamb, func_dist_y):
    # Pre-assign lists
    list_v = [0] * n_sample
    list_w = [0] * n_sample
    list_p = [0] * n_sample
    list_a = [0] * n_sample
    list_m = [0] * n_sample
    list_s = [0] * n_sample
    list_y = [0] * n_sample
    list_inter = [0] * n_sample
    # Initialization
    list_y[0] = func_dist_y()
    list_p[0] = 0
    list_a[0] = 0
    list_m[0] = 0
    for i in range(1, n_sample):
        list_inter[i] = random.expovariate(lamb)
        list_s[i] = list_s[i - 1] + list_inter[i]
        list_y[i] = func_dist_y()
        list_v[i], list_w[i], list_p[i], list_a[i], list_m[i] = cal(
            list_a[i - 1], list_m[i - 1], list_y[i], phi1, phi2)
    df = pd.DataFrame({
        'v': list_v,
        'w': list_w,
        'y': list_y,
        'p': list_p,
        'a': list_a,
        'm': list_m,
        's': list_s,
        'inter': list_inter
    })
    p_result = list_p[n_sample - 1]
    a_result = list_a[n_sample - 1]
    m_result = list_m[n_sample - 1]
    return df, p_result, a_result, m_result
