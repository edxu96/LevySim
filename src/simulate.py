# setup File for Levy Process
# author: Edward J. Xu
# date: 190624

import realize
import func_dist as fd
import visualize as vi
from functools import partial
import logging

########################################################################################################################


def select_dist(para):
    func = partial(fd.exp, lbd=para)
    return func


def single():
    """
    Plot the multiple simulation of a set of parameters
    """
    mu = 1  # mean = 1 / beta
    sigma = 1  # mean = 1 / beta
    lamb = 1  # mean = 1 / beta
    beta = 0.1
    n_sample = 1000
    n_sim = 100
    func_dist_y = select_dist(beta)
    _, _, _, mat_s, mat_p, mat_a, mat_m = realize.multi(mu, sigma, lamb, func_dist_y, n_sample, n_sim)
    vi.line_multi_pa(mat_s, mat_p, mat_a, '10')
    
    
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


def fpp_multi(list_a):
    """
    Calculate several first passage probability of multiple simulation
    """
    mu = 1
    sigma = 1
    lbd = 1
    beta = 1  # [beta in distribution of y], mean = 1 / beta
    n_sample = 1000
    n_sim = 1000
    func_dist_y = select_dist(beta)
    n_a = len(list_a)
    list_prob = [0] * n_a
    print("n_a = {}".format(n_a))
    for i in range(n_a):
        list_prob[i] = realize.multi(mu, sigma, lbd, func_dist_y, n_sample, n_sim, list_a[i])
    return list_prob
    # vi.line_fpp(list_a, list_prob, '8')





