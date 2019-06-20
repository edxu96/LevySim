# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import numpy as np
import matplotlib.pyplot as plt


def hist(list_result, num_bin, whe_show, name_fig):
    array_density, array_edge = np.histogram(list_result, bins=num_bin, density=True)
    len_edge = array_edge[1] - array_edge[0]
    list_density = [i * len_edge for i in array_density.tolist()]
    list_position = array_edge[0: (len(array_edge) - 1)]
    list_position = [i + len_edge / 2 for i in list_position]
    n_sample = len(list_result)
    fig = plt.figure(figsize=(18, 8))
    plt.plot(list_position, list_density)
    plt.xlabel('Class')
    plt.ylabel('Density')
    plt.title('Histogram of Result from {} Simulations'.format(n_sample), fontsize=15)
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')
    return list_density


def scatter_ap(list_t, list_p, list_a, whe_show, name_fig):
    fig = plt.figure(figsize=(18, 8))
    plt.scatter(list_t, list_p, label="pre-jump")
    plt.scatter(list_t, list_a, label="after-jump")
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend(loc='lower right')
    plt.title('Scatter Plot of Result from Simulations', fontsize=15)
    if whe_show:  # Whether to show the plot
        plt.show()
    fig.savefig('images/' + name_fig + '.png', bbox_inches='tight')


