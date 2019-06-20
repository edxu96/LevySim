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
        df, list_result = sl.sim(n_sample, mu, sigma, lamb, func_sim_dist, vec_para)
        list_p_result[i] = list_result[0]
        list_a_result[i] = list_result[1]
        list_m_result[i] = list_result[2]
    vi.hist(list_p_result, 30, False, '1')
    vi.hist(list_a_result, 30, False, '2')
    vi.hist(list_m_result, 30, False, '3')
    return list_p_result, list_a_result, list_m_result


def test():
    mu = 1
    sigma = 1
    lamb = 1
    n_sample = 100
    vec_para = 1
    func_sim_dist = lambda para: fd.exp(para)
    datf, list_result = sl.sim(n_sample, mu, sigma, lamb, func_sim_dist, vec_para)
    vi.scatter_ap(list_t=datf.t, list_p=datf.p, list_a=datf.a, whe_show=False, name_fig='4')
    print("p = {}".format(list_result[0]))
    print("a = {}".format(list_result[1]))
    print("m = {}".format(list_result[2]))


test()
list_p_result, list_a_result, list_m_result = task1()


