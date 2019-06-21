# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import numpy as np
from matplotlib import pyplot as plt
import logging


def hist(list_result, num_bin, name_fig, whe_show=False):
    array_density, array_edge = np.histogram(list_result, bins=num_bin, density=True)
    len_edge = array_edge[1] - array_edge[0]
    list_density = [i * len_edge for i in array_density.tolist()]
    list_position = array_edge[0: (len(array_edge) - 1)]
    list_position = [i + len_edge / 2 for i in list_position]
    n_sample = len(list_result)
    fig = plt.figure(figsize=(18, 8))
    plt.style.use("fivethirtyeight")
    plt.plot(list_position, list_density)
    plt.xlabel('Class')
    plt.ylabel('Density')
    plt.title('Histogram of Result from {} Simulations'.format(n_sample), fontsize=15)
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')
    return list_density


def jump_ap(list_s, list_p, list_a, list_m, name_fig, whe_show=False):
    fig = plt.figure(figsize=(18, 8))
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
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')


def line_apm(list_s, list_p, list_a, list_m, name_fig, whe_show=False):
    fig = plt.figure(figsize=(18, 8))
    plt.style.use("fivethirtyeight")
    n = len(list_s)
    list_result = [0] * 2 * n
    list_ss = [0] * 2 * n
    if not (n == len(list_p) and n == len(list_a)):
        logging.error("len(list_p) <> len(list_a)")
    for i in range(n):
        list_result[2 * i] = list_p[i]
        list_result[2 * i + 1] = list_a[i]
        list_ss[2 * i] = list_s[i]
        list_ss[2 * i + 1] = list_s[i]
    plt.plot(list_ss, list_result, label='X')
    plt.scatter(list_s, list_m, c='r', label='M')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Line Plot of Result from Simulations', fontsize=15)
    plt.legend()
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')
