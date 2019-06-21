# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import numpy as np
import scipy.stats as st
import random


def exp(beta):
    """
    Generate x from exponential distribution
        Built-in Python: pdf(x, beta) 1 / beta * exp(- x / beta)
    :param beta: parameter in desired exponential distribution, mean = 1 / beta
    :return: generated value
    """
    return random.expovariate(beta)

    
def erlang(shape):
    """

    :param shape:
    :return:
    """
    return st.erlang(shape).rvs()  # rvs(a, loc=0, scale=1, size=1, random_state=None)


def hyper_exp_2(p1, p2, beta):
    """
    Generate x from exponential distribution
        Built-in Python: pdf(x, beta) 1 / beta * exp(- x / beta)
    :param beta: parameter in desired exponential distribution, mean = 1 / beta
    :return: generated value
    """
    return random.expovariate(beta)

