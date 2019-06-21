# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import random


def exp(beta):
    """
    Generate x from exponential distribution
        Built-in Python: pdf(x, beta) 1 / beta * exp(- x / beta)
    :param beta: parameter in desired exponential distribution, mean = 1 / beta
    :return: generated value
    """
    return random.expovariate(beta)


