# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import sim_levy as sl
import func_dist as fd
import visualize as vi
from functools import partial
import time
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
    vi.jump_pa(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='4')
    vi.line_pam(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='5')
    # print("p = {}".format(list_result[0]))
    # print("a = {}".format(list_result[1]))
    # print("m = {}".format(list_result[2]))


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
    time_start = time.time()
    # your code
    _, _, list_m_result, _, _, _ = sl.sim_multi(mu, sigma, lamb, func_dist_y, n_sample, n_sim)
    prob = sum([i > a for i in list_m_result]) / len(list_m_result)
    time_elapse = time.time() - time_start
    print("Time elapsed = {} ;".format(time_elapse))
    return prob


def task1():
    mu = 1  # mean = 1 / beta
    sigma = 1  # mean = 1 / beta
    lamb = 1  # mean = 1 / beta
    beta = 1
    n_sample = 1000
    n_sim = 1000
    func_dist_y = select_dist(beta)
    list_p_result, list_a_result, list_m_result, _, _, _, _ = sl.sim_multi(mu, sigma, lamb, func_dist_y, n_sample, n_sim)
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
    # list_a = [10, 100, 1000, 10000, 100000, 1000000]
    # list_a = list(range(500, 10000, 100))
    # list_a = list(range(2000, 4000, 100))
    list_a = list(range(2750, 3250, 50))
    n_a = len(list_a)
    list_prob = [0] * n_a
    print("n_a = {}".format(n_a))
    for i in range(n_a):
        list_prob[i] = cal_fpp(mu, sigma, lamb, func_dist_y, n_sample, n_sim, list_a[i])
    vi.line_fpp(list_a, list_prob, '8')


def task3():
    """
    Plot the multiple simulation of a set of parameters
    :return:
    """
    mu = 1  # mean = 1 / beta
    sigma = 1  # mean = 1 / beta
    lamb = 1  # mean = 1 / beta
    beta = 0.1
    n_sample = 1000
    n_sim = 100
    func_dist_y = select_dist(beta)
    _, _, _, mat_s, mat_p, mat_a, mat_m = sl.sim_multi(mu, sigma, lamb, func_dist_y, n_sample, n_sim)
    vi.line_multi_pa(mat_s, mat_p, mat_a, '10')


def task3_2dim():
    mu = 1  # mean = 1 / beta
    sigma = 1  # mean = 1 / beta
    lamb = 1  # mean = 1 / beta
    n_sample = 1000
    n_sim = 100
    # Different beta s
    beta_1 = 0.1
    beta_2 = 1
    func_dist_y_1 = select_dist(beta_1)
    func_dist_y_2 = select_dist(beta_2)
    # Simulation
    _, _, _, mat_s_1, mat_p_1, mat_a_1, _ = sl.sim_multi(mu, sigma, lamb, func_dist_y_1, n_sample, n_sim)
    _, _, _, mat_s_2, mat_p_2, mat_a_2, _ = sl.sim_multi(mu, sigma, lamb, func_dist_y_2, n_sample, n_sim)
    # Plot the result
    vi.line_multi_pa_2(mat_s_1, mat_p_1, mat_a_1, mat_s_2, mat_p_2, mat_a_2, '11')


def main():
    # test()
    # task1()
    # task2()
    # task3()
    task3_2dim()


main()


