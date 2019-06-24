

import realize
import simulate
import visualize as vi

########################################################################################################################

def do1():
    mu = 1
    sigma = 1
    lbd = 1
    beta = 1
    n_sample = 1000
    n_sim = 1000
    func_dist_y = simulate.select_dist(beta)
    list_p_result, list_a_result, list_m_result, _, _, _, _ = realize.multi(
        mu, sigma, lbd, func_dist_y, n_sample, n_sim)
    vi.hist(list_p_result, 30, 'p', '1')
    vi.hist(list_a_result, 30, 'a', '2')
    vi.hist(list_m_result, 30, 'm', '3')


def do5(name_fig):
    # list_a = [10, 100, 1000, 10000, 100000, 1000000]
    # list_a = list(range(500, 10000, 100))
    # list_a = list(range(2000, 4000, 100))
    list_a = list(range(2750, 3250, 50))
    list_prob = simulate.fpp_multi(list_a)
    vi.line_fpp_multi(list_a, list_prob, name_fig)


