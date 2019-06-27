# setup File for Levy Process
# author: Edward J. Xu, Aijie Shu
# date: 190620

import scipy.stats as st
import numpy as np
import random

########################################################################################################################


def exp(lbd):
    """
    Generate x from exponential distribution
        Built-in Python: pdf = lambda * exp(-lambda * x)
    :param lbd: parameter in desired exponential distribution, lamda = 1 / mean
    :return: generated value once
    """
    # mean = 1 / lbd
    # return st.expon(scale=mean).rvs(size=1)[0]
    return random.expovariate(lbd)


def erlang(shape, scale):
    """
    Generate x from exponential distribution
        Built-in Python: pdf = f(x ; k, \mu) =\frac{x^{k-1} e^{-\frac{x}{\mu}}}{\mu^{k}(k-1) !} \quad
        \text { for } x, \mu \geq 0
    :param shape: when shape parameter k equals one, it simplifies to the exponential distribution.
    :return: generated value once
    """
    return st.erlang(a = shape, scale = scale).rvs(size=1)[0]


def hyperexp(p1, lbd1, p2, lbd2):
    """
    Generate x from two exponetial distribution and accept one of them with probability
        Build-in Python: pdf = f_{X}(x)=\sum_{i=1}^{n} f_{Y_{i}}(x) p_{i}
    
    :param p1: probability to choose type 1
           lbd1: the lambda value of type 1's exponential distribution
           p1: probability to choose type 2
           lbd2: the lambda value of type 2's exponential distribution
           remind!!!!! scale can only be
           
    : return: generated value once
    """
    return np.random.choice(a=[random.expovariate(lbd1), random.expovariate(lbd2)], size=1, p=[p1, 1-p1])[0]


def pareto(alpha, scale):
    """
    Generate x from pareto distribution
        Built-in Python: pdf = f_{X}(x)=\left\{\begin{array}{ll}{\frac{\alpha x_{\mathrm{m}}^{\alpha}}{x^{\alpha+1}}} &
        {x \geq x_{\mathrm{m}}} \\ {0} & {x<x_{\mathrm{m}}}\end{array}\right.
	"""
    return st.pareto(b = alpha, scale = scale).rvs(size = 1)[0]



