# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import random


def exp(lamb):
    """
    Generate x from exponential distribution
    pdf(x, lambda) 1 / beta * exp(- x / beta)
    mean = lambda = 1 / beta
    :param lamb:
    :return:
    """
    return random.expovariate(lamb)


