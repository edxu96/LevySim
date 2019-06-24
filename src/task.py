

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


def do3():
    n_sample = 100
    n_sim = 10
    # Different beta s
    list_beta = [1, 1, 1]
    list_mu = [0.1, 1, 10]
    list_sigma = [1, 1, 1]
    list_lbd = [1, 1, 1]
    # Begin Simulation
    simulate.multi(n_sample, n_sim, list_beta, list_mu, list_sigma, list_lbd, '4')
    # Different sigma
    list_beta = [1, 1, 1]
    list_mu = [1, 1, 1]
    list_sigma = [0.1, 1, 10]
    list_lbd = [1, 1, 1]
    # Begin Simulation
    simulate.multi(n_sample, n_sim, list_beta, list_mu, list_sigma, list_lbd, '5')
    # Different lambda
    list_beta = [1, 1, 1]
    list_mu = [1, 1, 1]
    list_sigma = [1, 1, 1]
    list_lbd = [0.1, 1, 10]
    # Begin Simulation
    simulate.multi(n_sample, n_sim, list_beta, list_mu, list_sigma, list_lbd, '6')


def do5(name_fig):
    # list_a = [10, 100, 1000, 10000, 100000, 1000000]
    # list_a = list(range(500, 10000, 100))
    # list_a = list(range(2000, 4000, 100))
    list_a = list(range(2750, 3250, 50))
    list_prob = simulate.fpp_multi(list_a)
    vi.line_fpp_multi(list_a, list_prob, name_fig)


def test():
    mu = 1
    sigma = 1
    n_sample = 100
    lbd = 1
    beta = 1  # [beta in distribution of y],
    func_dist_y = simulate.select_dist(beta)
    df, list_result = realize.single(n_sample, mu, sigma, lbd, func_dist_y)
    # Visualize and print the result
    vi.jump_pa(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='01')
    vi.line_pam(list_s=df.s, list_p=df.p, list_a=df.a, list_m=df.m, name_fig='02')
    print("p = {}".format(list_result[0]))
    print("a = {}".format(list_result[1]))
    print("m = {}".format(list_result[2]))

