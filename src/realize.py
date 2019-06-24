# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import random
import pandas as pd
import numpy as np
import time
from numbers import Number
import logging
import scipy.stats as st

########################################################################################################################


def update(a_pre, m_pre, y, phi1, phi2):
    """
    Update the value of v, w, p, a, m
    """
    v = random.expovariate(phi1)  # st.expon(scale=1 / phi1).rvs(size=1)[0]
    w = random.expovariate(phi2)  # st.expon(scale=1 / phi2).rvs(size=1)[0]
    p = a_pre + (v - w)
    a = a_pre + (v - w) + y
    m = max(m_pre, a_pre + v, a)
    return v, w, p, a, m


def single(n_sample, phi1, phi2, lbd, func_dist_y):
    """
    Do simulation using same set of parameters
    """
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
    # Being Simulation
    for i in range(1, n_sample):
        list_inter[i] = random.expovariate(lbd)  # st.expon(scale=1 / lbd).rvs(size=1)[0]
        list_s[i] = list_s[i - 1] + list_inter[i]
        list_y[i] = func_dist_y()
        list_v[i], list_w[i], list_p[i], list_a[i], list_m[i] = update(
            list_a[i - 1], list_m[i - 1], list_y[i], phi1, phi2)
    # Store all the result in dataframe
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
    p_result = list_p[-1]
    a_result = list_a[-1]
    m_result = list_m[-1]
    return df, p_result, a_result, m_result


def multi(mu, sigma, lbd, func_dist_y, n_sample, n_sim, a=False):
    """
    Do multiple simulation using same set of parameters, and calculate the first passage probability
    """
    # Calculate phi
    phi1 = - mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lbd / sigma ** 2)
    phi2 = mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lbd / sigma ** 2)
    # Initialize lists
    list_p_result = [0] * n_sim
    list_a_result = [0] * n_sim
    list_m_result = [0] * n_sim
    mat_s = np.zeros((n_sim, n_sample))
    mat_p = np.zeros((n_sim, n_sample))
    mat_a = np.zeros((n_sim, n_sample))
    mat_m = np.zeros((n_sim, n_sample))
    # Start simulation
    time_start = time.time()
    for i in range(n_sim):
        df, list_p_result[i], list_a_result[i], list_m_result[i] = single(n_sample, phi1, phi2, lbd, func_dist_y)
        mat_s[i, :] = df.s
        mat_p[i, :] = df.p
        mat_a[i, :] = df.a
        mat_m[i, :] = df.m
    time_elapse = time.time() - time_start
    print("Time elapsed = {} ;".format(time_elapse))
    # Calculate first passage probability given a of sim.multi
    if not a:
        fpp = None
    elif isinstance(a, Number):
        fpp = sum([i > a for i in list_m_result]) / len(list_m_result)
    else:
        logging.error("Wrong `a` input!")
        fpp = None
    return list_p_result, list_a_result, list_m_result, mat_s, mat_p, mat_a, mat_m, fpp


