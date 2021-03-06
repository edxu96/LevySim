# setup File for Levy Process
# author: Edward J. Xu
# date: 190624

import realize
import func_dist as fd
import visualize as vi
from functools import partial
import logging


def select_dist(para):
    func = partial(fd.exp, lbd=para)
    return func


def select_dist_erlang(shape, scale):
    func = partial(fd.erlang, shape=shape, scale = scale)
    return func


def select_dist_hyperexpon(p1, lbd1, p2, lbd2):
    func = partial(fd.hyperexp, p1=p1, lbd1=lbd1, p2=p2, lbd2=lbd2)
    return func


def select_dist_pareto(alpha, scale):
    func = partial(fd.pareto, alpha=alpha, scale=scale)
    return func


def check_len(list_list):
    """
    Check if the lengths of lists in the list_list are the same
    """
    n_check = len(list_list)
    length = len(list_list[1])
    if sum([len(j) == length for j in list_list]) != n_check:
        logging.error("Length of lists of parameters are not equal!")
        quit()


def multi(n_sample, n_sim, list_beta, list_mu, list_sigma, list_lbd, str_fig):
    """
    Combine simulation result of different sets of parameters
    """
    n_set = len(list_beta)
    check_len([list_beta, list_mu, list_sigma, list_lbd])
    # Initialize the lists for result
    list_mat_s = [None] * n_set
    list_mat_p = [None] * n_set
    list_mat_a = [None] * n_set
    # Being Simulation
    for i in range(n_set):
        _, _, _, list_mat_s[i], list_mat_p[i], list_mat_a[i], _, _ = realize.multi(
            list_mu[i], list_sigma[i], list_lbd[i], select_dist(list_beta[i]), n_sample, n_sim)
    # Plot the result
    vi.line_simulate_multi(list_mat_s, list_mat_p, list_mat_a, str_fig)


def fpp_multi(mu, sigma, lbd, func_dist_y, n_sample, n_sim, list_a):
    """
    Calculate several first passage probability of multiple simulation
    """
    print("--------------------------------------------------------------------------------\n"
          "Calculate First Passage Probabilities of Different a")
    _, _, list_m_result, _, _, _, _, _ = realize.multi(mu, sigma, lbd, func_dist_y, n_sample, n_sim)
    n_a = len(list_a)
    list_fpp = [0] * n_a
    for j in range(n_a):
        list_fpp[j] = sum([i > list_a[j] for i in list_m_result]) / len(list_m_result)
    return list_fpp


def fpp_series(mu, sigma, lbd, func_dist_y, n_sample, n_sim, n_a_raw):
    print("--------------------------------------------------------------------------------\n"
          "Calculate First Passage Probabilities of Different a")
    _, _, list_m_result, mat_s, mat_p, mat_a, _, _ = realize.multi(mu, sigma, lbd, func_dist_y, n_sample, n_sim)
    step = (max(list_m_result) - min(list_m_result)) / n_a_raw
    list_a = [0] * (n_a_raw + 6)
    for i in range(n_a_raw + 6):
        list_a[i] = min(list_m_result) + step * (i - 3)
    n_a = len(list_a)
    list_fpp = [0] * n_a
    for j in range(n_a):
        list_fpp[j] = sum([i > list_a[j] for i in list_m_result]) / len(list_m_result)
    return list_a, list_fpp, mat_s, mat_p, mat_a


def fpp_series_multi(mu, sigma, lbd, list_func_dist_y, n_sample, n_sim, n_a_raw):
    n_dist = len(list_func_dist_y)
    list_list_a = [None] * n_dist
    list_list_fpp = [None] * n_dist
    for i in range(n_dist):
        list_list_a[i], list_list_fpp[i], _, _, _ = fpp_series(
            mu, sigma, lbd, list_func_dist_y[i], n_sample, n_sim, n_a_raw)
    return list_list_a, list_list_fpp
