# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import numpy as np
from matplotlib import pyplot as plt
import logging


def get_pdf(list_result, num_bin):
    """
    Get position and value for prob density function.
    :param list_result: list of result
    :param num_bin: number of bins for the plot
    :return:
    """
    array_density, array_edge = np.histogram(list_result, bins=num_bin, density=True)
    len_edge = array_edge[1] - array_edge[0]
    list_density = [i / len_edge for i in array_density.tolist()]
    print("sum(list_density) = {} ;".format(sum(list_density)))
    list_position = array_edge[0: (len(array_edge) - 1)]
    list_position = [i + len_edge / 2 for i in list_position]
    return list_position, list_density


def hist(list_result, num_bin, str_var, name_fig, whe_show=False):
    """
    Plot the histogram using line.
    :param list_result:
    :param num_bin:
    :param str_var: name string of the variable
    :param name_fig: name string of the figure
    :param whe_show: whether to show the plot
    :return:
    """
    list_position, list_density = get_pdf(list_result, num_bin)
    n_sim = len(list_result)
    fig = plt.figure(figsize=(10, 8))
    plt.style.use("fivethirtyeight")
    plt.plot(list_position, list_density)
    plt.xlabel('Class')
    plt.ylabel('Density')
    plt.title('Histogram of {} from {} Simulations'.format(str_var, n_sim), fontsize=15)
    plt.tight_layout()
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')
    return list_density


def jump_pa(list_s, list_p, list_a, list_m, name_fig, whe_show=False):
    """
    Scatter plot of all the jumps
    """
    fig = plt.figure(figsize=(10, 8))
    # plt.xkcd()
    plt.style.use("fivethirtyeight")
    for i in range(len(list_s)):
        plt.plot([list_s[i], list_s[i]], [list_p[i], list_a[i]], c='silver', linewidth=0.5)
    plt.scatter(list_s, list_p, label="p: pre-jump")
    plt.scatter(list_s, list_a, label="a: after-jump")
    plt.plot(list_s, list_m, c='red', label='m: max X so far')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()  # loc='upper right'
    plt.title('Scatter Plot of Result from Simulations', fontsize=15)
    plt.tight_layout()
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')


def inter_pa(list_s, list_p, list_a):
    """
    Obtain the list like "p_1, a_1, p_2, a_2, p_3, a_3, ..." from list of p and a
    :param list_s:
    :param list_a:
    :param list_p:
    :return: list_ss: list like "s_1, s_1, s_2, s_2, s_3, s_3, ..."
    """
    n = len(list_s)
    list_pa = [0] * 2 * n
    list_ss = [0] * 2 * n
    if not (n == len(list_p) and n == len(list_a)):
        logging.error("len(list_s), len(list_p) and len(list_a) are not equal!")
    for i in range(n):
        list_pa[2 * i] = list_p[i]
        list_pa[2 * i + 1] = list_a[i]
        list_ss[2 * i] = list_s[i]
        list_ss[2 * i + 1] = list_s[i]
    return list_ss, list_pa


def line_pam(list_s, list_p, list_a, list_m, name_fig, whe_show=False):
    """
    Line plot of the realization
    :param list_s:
    :param list_p:
    :param list_a:
    :param list_m:
    :param name_fig:
    :param whe_show:
    :return:
    """
    fig = plt.figure(figsize=(10, 8))
    plt.style.use("fivethirtyeight")
    list_ss, list_pa = inter_pa(list_s, list_p, list_a)
    plt.plot(list_ss, list_pa, label='X')
    plt.scatter(list_s, list_m, c='r', label='M')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Line Plot of Result from Simulations', fontsize=15)
    plt.legend()
    plt.tight_layout()
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')


def line_fpp(list_a, list_prob, name_fig, whe_show=False):
    fig = plt.figure(figsize=(10, 8))
    plt.style.use("fivethirtyeight")
    plt.plot(list_a, list_prob)  # , linestyle='--', marker='o'
    plt.xlabel('a')
    plt.ylabel('Probability')
    # plt.xticks(ticks=list_a, labels=list_a)
    # plt.annotate(
    #     'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
    #     xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))
    plt.title('Line Plot of First Passage Probability under Different a', fontsize=15)
    plt.tight_layout()
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')


def line_fpp_multi(list_list_a, list_list_prob, list_label, name_fig, whe_show=False):
    fig = plt.figure(figsize=(10, 8))
    plt.style.use("fivethirtyeight")
    for i in range(len(list_list_a)):
        plt.plot(list_list_a[i], list_list_prob[i], label=list_label[i])  # , linestyle='--', marker='o'
    plt.xlabel('a')
    plt.ylabel('Probability')
    # plt.xticks(ticks=list_a, labels=list_a)
    # plt.annotate(
    #     'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
    #     xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))
    plt.title('Line Plot of First Passage Probability under Different a', fontsize=15)
    plt.legend()
    plt.tight_layout()
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')


def line_multi_pa(mat_s, mat_p, mat_a, name_fig, whe_show=False):
    n_sim = len(mat_p[:, 1])
    if n_sim != len(mat_a[:, 1]):
        logging.error("len(mat_p[:, 1]) and len(mat_a[:, 1]) are not equal!")
    fig = plt.figure(figsize=(10, 8))
    plt.style.use("fivethirtyeight")
    for i in range(n_sim):
        list_ss, list_pa = inter_pa(mat_s[i, :], mat_p[i, :], mat_a[i, :])
        plt.plot(list_ss, list_pa, linewidth=0.5, c='gray')
    plt.xlabel('arrival time')
    plt.ylabel('value of X prior to and after jump')
    plt.title('Line Plot of Multiple Realization', fontsize=15)
    plt.tight_layout()
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')


def get_list_color(n_set):
    """
    Get the list with enough number of colors
    :param n_set:
    :return:
    """
    list_color_raw = ['tomato', 'lightskyblue', 'wheat', 'limegreen', 'violet']
    list_color = ['tomato', 'lightskyblue', 'wheat', 'limegreen', 'violet']
    k = 2
    while len(list_color) < n_set:
        list_color = list_color_raw * k
        k = k + 1
        print(k)
    return list_color


def line_simulate_multi(list_mat_s, list_mat_p, list_mat_a, name_fig, whe_show=False):
    n_set = len(list_mat_s)
    n_sim = len(list_mat_p[1][:, 1])
    # if n_sim != len(mat_a_1[:, 1]):
    #     logging.error("len(mat_p[:, 1]) and len(mat_a[:, 1]) are not equal!")
    fig = plt.figure(figsize=(10, 8))
    plt.style.use("fivethirtyeight")
    list_color = get_list_color(n_set)
    # Plot the lines
    for j in range(n_set):
        for i in range(n_sim):
            list_ss, list_pa = inter_pa(list_mat_s[j][i, :], list_mat_p[j][i, :], list_mat_a[j][i, :])
            plt.plot(list_ss, list_pa, linewidth=0.5, c=list_color[j])
    plt.xlabel('arrival time')
    plt.ylabel('value of X prior to and after jump')
    plt.title('Line Plot of Simulations with Different Sets of Parameters', fontsize=15)
    plt.tight_layout()
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')

