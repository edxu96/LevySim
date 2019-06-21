# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import random
import pandas as pd
import numpy as np


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


def sim_multi(mu, sigma, lamb, func_dist_y, n_sample, n_sim):
    # Calculate phi
    phi1 = mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lamb / sigma ** 2)
    phi2 = - mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lamb / sigma ** 2)
    #
    list_p_result = [0] * n_sim
    list_a_result = [0] * n_sim
    list_m_result = [0] * n_sim
    mat_s = np.zeros((n_sim, n_sample))
    mat_p = np.zeros((n_sim, n_sample))
    mat_a = np.zeros((n_sim, n_sample))
    mat_m = np.zeros((n_sim, n_sample))
    for i in range(n_sim):
        df, list_p_result[i], list_a_result[i], list_m_result[i] = sim(n_sample, phi1, phi2, lamb, func_dist_y)
        mat_s[i, :] = df.s
        mat_p[i, :] = df.p
        mat_a[i, :] = df.a
        mat_m[i, :] = df.m
    return list_p_result, list_a_result, list_m_result, mat_s, mat_p, mat_a, mat_m

