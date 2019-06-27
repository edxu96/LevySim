# setup File for Levy Process
# author: Edward J. Xu
# date: 190624

import realize
import simulate
import visualize as vi
import numpy as np
import random
import scipy.stats as st

########################################################################################################################


def do1():
    mu = 1
    sigma = 1
    lbd = 1
    beta = 1
    n_sample = 1000
    n_sim = 1000
    func_dist_y = simulate.select_dist(beta)
    list_p_result, list_a_result, list_m_result, _, _, _, _, _ = realize.multi(
        mu, sigma, lbd, func_dist_y, n_sample, n_sim)
    vi.hist(list_p_result, 30, 'p', 'task1-1')
    vi.hist(list_a_result, 30, 'a', 'task1-2')
    vi.hist(list_m_result, 30, 'm', 'task1-3')


def do3():
    n_sample = 1000
    n_sim = 100
    # Different mu
    list_beta = [1, 1, 1]
    list_mu = [-10, 1, 10]
    list_sigma = [1, 1, 1]
    list_lbd = [1, 1, 1]
    simulate.multi(n_sample, n_sim, list_beta, list_mu, list_sigma, list_lbd, 'task3-mu')
    # Different sigma
    # list_beta = [1, 1, 1]
    # list_mu = [1, 1, 1]
    # list_sigma = [0.1, 1, 1000]
    # list_lbd = [1, 1, 1]
    # simulate.multi(n_sample, n_sim, list_beta, list_mu, list_sigma, list_lbd, 'task3-sigma')
    # Different lambda
    # list_beta = [1, 1, 1]
    # list_mu = [1, 1, 1]
    # list_sigma = [1, 1, 1]
    # list_lbd = [0.1, 1, 10]
    # simulate.multi(n_sample, n_sim, list_beta, list_mu, list_sigma, list_lbd, 'task3-lbd')

    
def do4():
    """
    Plot the multiple simulation on different Y distribution
    """
    mu = 1
    sigma = 1
    lbd = 1
    n_sample = 1000
    n_sim = 10
    list_func_dist_y = [simulate.select_dist(1), simulate.select_dist_erlang(shape = 10, scale = 1/10),simulate.select_dist_hyperexpon(0.2, 1/4, 0.8, 4), simulate.select_dist_pareto(5, 4/5)]
    for i in range(len(list_func_dist_y)):
        _, _, _, mat_s, mat_p, mat_a, mat_m, _ = realize.multi(mu, sigma, lbd, list_func_dist_y[i], n_sample, n_sim)
        vi.line_multi_pa(mat_s, mat_p, mat_a, 'task4-' + str(i))


def do5_1(mu, sigma, lbd, beta, n_sample, n_sim):
    list_a = [1, 10, 1000, 100000]
    # list_a = list(range(2750, 3250, 50))
    # list_a = [1]
    func_dist_y = simulate.select_dist(beta)
    # Being Simulation
    list_fpp = simulate.fpp_multi(mu, sigma, lbd, func_dist_y, n_sample, n_sim, list_a)
    print("    list_a = {} ;".format(list_a))
    print("    list_fpp = {} ;".format(list_fpp))


def do5_2(mu, sigma, lbd, beta, n_sample, n_sim, n_a_raw):
    func_dist_y = simulate.select_dist(beta)
    list_a, list_fpp, mat_s, mat_p, mat_a = simulate.fpp_series(
        mu, sigma, lbd, func_dist_y, n_sample, n_sim, n_a_raw)
    vi.line_fpp(list_a, list_fpp, 'task5-2')
    vi.line_multi_pa(mat_s, mat_p, mat_a, 'task5-3')


def do5_3(mu, sigma, lbd, n_sample, n_sim, n_a_raw):
    list_func_dist_y = [simulate.select_dist(1), simulate.select_dist_erlang(shape = 10, scale = 1/10),
                        simulate.select_dist_hyperexpon(0.2, 1/4, 0.8, 4), simulate.select_dist_pareto(5,4/5 )]
    list_label = ['Exp', 'Erland', 'Hyper-Exp', 'Pareto']
    list_list_a, list_list_fpp = simulate.fpp_series_multi(mu, sigma, lbd, list_func_dist_y, n_sample, n_sim, n_a_raw)
    vi.line_fpp_multi(list_list_a, list_list_fpp, list_label, 'task5-4')


def do5():
    # 1,  Set Parameters
    mu = -1
    sigma = 1
    lbd = 1
    beta = 1  # [beta in distribution of y], mean = 1 / beta
    n_sample = 1000
    n_sim = 100
    # 2,  Task 5.1: Calculate fpp under different a
    #do5_1(mu, sigma, lbd, beta, n_sample, n_sim)
    # 3,  Task 5.2: Plot the fpp as line with exponential distribution
    n_a_raw = 20
    do5_2(mu, sigma, lbd, beta, n_sample, n_sim, n_a_raw)
    # 4,  Task 5.3: Plot the fpp as lines with different distributions
    n_a_raw = 20
    do5_3(mu, sigma, lbd, n_sample, n_sim, n_a_raw)


def test():
    mu = 1
    sigma = 1
    n_sample = 1000
    lbd = 1
    beta = 1  # [beta in distribution of y],
    func_dist_y = simulate.select_dist(beta)
    phi1 = - mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lbd / sigma ** 2)
    phi2 = mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 + 2 * lbd / sigma ** 2)
    print("phi1 = {} ;".format(phi1))
    print("phi2 = {} ;".format(phi2))
    df, p_result, a_result, m_result = realize.single(n_sample, phi1, phi2, lbd, func_dist_y)
    # Visualize and print the result
    vi.jump_pa(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='test-1')
    vi.line_pam(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='test-2')
    print("p = {} ;".format(p_result))
    print("a = {} ;".format(a_result))
    print("m = {} ;".format(m_result))


def test_dist_exp(mean):
    print("mean = {} ;".format(mean))
    lbd = 1 / mean
    list_result1 = [0] * 10000
    list_result2 = [0] * 10000
    list_result3 = [0] * 10000
    for i in range(10000):
        list_result1[i] = random.expovariate(lbd)
        list_result2[i] = st.expon(scale=1 / lbd).rvs(size=1)[0]
        list_result3[i] = np.random.choice(a=[random.expovariate(lbd), random.expovariate(lbd)], size=1,
                                           p=[0.5, 0.5])[0]
    print(sum(list_result1) / 10000)
    print(sum(list_result2) / 10000)
    print(sum(list_result3) / 10000)


