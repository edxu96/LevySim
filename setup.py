# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import sim_levy as sl
import func_dist as fd
# import scipy.stats as stats
# import matplotlib.pyplot as plt


def test():
    mu = 1
    sigma = 1
    lamb = 1
    num_sim = 100
    vec_para = 1
    func_sim_dist = lambda para: fd.exp(para)
    p, a, m = sl.sim(num_sim, mu, sigma, lamb, func_sim_dist, vec_para)
    print("p = {}".format(p))
    print("a = {}".format(a))
    print("m = {}".format(m))


test()