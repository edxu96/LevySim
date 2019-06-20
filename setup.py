# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import SimLevy


def test():
    mu = 1
    sigma = 1
    lamb = 1
    lamb_y = 1
    num_sim = 100
    p, a, m = SimLevy.sim(num_sim, mu, sigma, lamb, lamb_y)
    print("p = {}".format(p))
    print("a = {}".format(a))
    print("m = {}".format(m))


test()