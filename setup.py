# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import sim_levy as sl
import func_dist as fd
import visualize as vi
from functools import partial
import numpy as np
# import scipy.stats as stats


def select_dist(para):
    func = partial(fd.exp, beta=para)
    return func


def test():
    mu = 1
    sigma = 1
    n_sample = 100
    lamb = 1
    beta = 1  # [beta in distribution of y],
    func_dist_y = select_dist(beta)
    df, list_result = sl.sim(n_sample, mu, sigma, lamb, func_dist_y)
    vi.jump_ap(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='4')
    vi.line_apm(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='5')
    # print("p = {}".format(list_result[0]))
    # print("a = {}".format(list_result[1]))
    # print("m = {}".format(list_result[2]))


def sim_multi(mu, sigma, lamb, func_dist_y, n_sample, n_sim):
    # Calculate phi
    phi1 = mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lamb / sigma ** 2)
    phi2 = - mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lamb / sigma ** 2)
    #
    list_p_result = [0] * n_sim
    list_a_result = [0] * n_sim
    list_m_result = [0] * n_sim
    for i in range(n_sim):
        _, list_p_result[i], list_a_result[i], list_m_result[i] = sl.sim(n_sample, phi1, phi2, lamb, func_dist_y)
    return list_p_result, list_a_result, list_m_result


def cal_fpp(mu, sigma, lamb, func_dist_y, n_sample, n_sim, a):
    """
    Calculate first passage probability
    :param mu:
    :param sigma:
    :param lamb:
    :param func_dist_y:
    :param n_sample:
    :param n_sim:
    :param a:
    :return:
    """
    _, _, list_m_result = sim_multi(mu, sigma, lamb, func_dist_y, n_sample, n_sim)
    prob = sum([i > a for i in list_m_result]) / len(list_m_result)
    return prob


def task1():
    mu = 1  # mean = 1 / beta
    sigma = 1  # mean = 1 / beta
    lamb = 1  # mean = 1 / beta
    beta = 1
    n_sample = 1000
    n_sim = 1000
    func_dist_y = select_dist(beta)
    list_p_result, list_a_result, list_m_result = sim_multi(mu, sigma, lamb, func_dist_y, n_sample, n_sim)
    vi.hist(list_p_result, 30, 'p', '1')
    vi.hist(list_a_result, 30, 'a', '2')
    vi.hist(list_m_result, 30, 'm', '3')


def task2():
    mu = 1  # mean = 1 / beta
    sigma = 1  # mean = 1 / beta
    lamb = 1  # mean = 1 / beta
    beta = 1  # [beta in distribution of y], mean = 1 / beta
    n_sample = 1000
    n_sim = 1000
    func_dist_y = select_dist(beta)
    list_a = [10, 100, 1000]
    # list_a = list(range(100, 2000, 50))
    list_prob = [0] * len(list_a)
    for i in range(len(list_a)):
        list_prob[i] = cal_fpp(mu, sigma, lamb, func_dist_y, n_sample, n_sim, list_a[i])
    vi.line_fpp(list_a, list_prob, '6')


def main():
    # test()
    # task1()
    task2()


main()


