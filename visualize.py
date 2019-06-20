# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import numpy as np
import matplotlib.pyplot as plt


def hist(list):
    list_density, list_count = np.histogram(list, bins=10, density=True)
    plt.plot(list_density)
    return list_density


def line(list_t, list_p, list_a):
    plt.scatter(list_t, list_p)
    plt.scatter(list_t, list_a)
    plt.show()


