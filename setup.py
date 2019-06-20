# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import sim_levy as sl
import func_dist as fd
import visualize as vi
# import scipy.stats as stats
# import matplotlib.pyplot as plt


def task1():
    mu = 1
    sigma = 1
    lamb = 1
    n_sample = 100
    vec_para = 1
    func_sim_dist = lambda para: fd.exp(para)
    n_sim = 100
    list_p_result = [0] * n_sim
    list_a_result = [0] * n_sim
    list_m_result = [0] * n_sim
    for i in range(n_sim):
        list_p_result[i], list_a_result[i], list_m_result[i] = sl.sim(
            n_sample, mu, sigma, lamb, func_sim_dist, vec_para)
    vi.hist(list_p_result)
    vi.hist(list_a_result)
    vi.hist(list_m_result)
    return list_p_result, list_a_result, list_m_result


def test():
    mu = 1
    sigma = 1
    lamb = 1
    n_sample = 100
    vec_para = 1
    func_sim_dist = lambda para: fd.exp(para)
    p, a, m = sl.sim(n_sample, mu, sigma, lamb, func_sim_dist, vec_para)
    print("p = {}".format(p))
    print("a = {}".format(a))
    print("m = {}".format(m))


# test()
list_p_result, list_a_result, list_m_result = task1()