# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import random


def exp(mean):
    """
    Generate x from exponential distribution
        Built-in Python: pdf(x, beta) 1 / beta * exp(- x / beta)
        mean = 1 / beta
    :param mean: mean of the desired exponential distribution
    :return: generated value
    """
    return random.expovariate(1 / mean)


