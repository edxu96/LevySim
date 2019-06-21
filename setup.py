# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import sim_levy as sl
import func_dist as fd
import visualize as vi
from functools import partial
# import scipy.stats as stats
# import matplotlib.pyplot as plt


def select_dist(lamb):
    func = partial(fd.exp, lamb=lamb)
    return func


def task1():
    mu = 1
    sigma = 1
    lamb = 1
    n_sample = 100
    func_dist_y = select_dist(lamb)
    n_sim = 100
    list_p_result = [0] * n_sim
    list_a_result = [0] * n_sim
    list_m_result = [0] * n_sim
    for i in range(n_sim):
        df, list_result = sl.sim(n_sample, mu, sigma, lamb, func_dist_y)
        list_p_result[i] = list_result[0]
        list_a_result[i] = list_result[1]
        list_m_result[i] = list_result[2]
    vi.hist(list_p_result, 30, '1')
    vi.hist(list_a_result, 30, '2')
    vi.hist(list_m_result, 30, '3')
    return list_p_result, list_a_result, list_m_result


def test():
    mu = 1
    sigma = 1
    n_sample = 100
    lamb = 1
    func_dist_y = select_dist(lamb)
    df, list_result = sl.sim(n_sample, mu, sigma, lamb, func_dist_y)
    vi.jump_ap(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='4')
    # vi.line_apm(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='5')
    # print("p = {}".format(list_result[0]))
    # print("a = {}".format(list_result[1]))
    # print("m = {}".format(list_result[2]))


test()
# list_p_result, list_a_result, list_m_result = task1()


