# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import scipy.stats as st
import numpy as np

def exp(lbd):
    """
    Generate x from exponential distribution
        Built-in Python: pdf = lambda * exp(-lambda * x)
    :param lbd: parameter in desired exponential distribution, lamda = 1 / mean
    :return: generated value once
    """
    return st.expon(scale=1 /lbd).rvs(size=1)


def erlang(shape):
    """
    Generate x from exponential distribution
        Built-in Python: pdf = f(x ; k, \mu) =\frac{x^{k-1} e^{-\frac{x}{\mu}}}{\mu^{k}(k-1) !} \quad \text { for } x, \mu \geq 0
    :param shape: when shape parameter k equals one, it simplifies to the exponential distribution.
    :return: generated value once
    """
    return st.erlang(shape).rvs(size=1)


def hyperexp(p1, lbd1, p2, lbd2):
    """
    Generate x from two exponetial distribution and accept one of them with probability
        Build-in Python: pdf = f_{X}(x)=\sum_{i=1}^{n} f_{Y_{i}}(x) p_{i}
    
    :param p1: probability to choose type 1
<<<<<<< HEAD:func_dist.py
           lamda1: the lambda value of type 1's exponential distribution
           p1: probability to choose type 2
           lamda1: the lambda value of type 2's exponential distribution
           remind!!!!! scale can only be
           
    : return: generated value once
    """

    return np.random.choice(a = [st.expon.rvs(scale = 1/lbd1), st.expon.rvs(scale = 1/lbd2)],size = 1, p = [p1, 1-p1])
=======
    :param lbd1: the lambda value of type 1's exponential distribution
    :param p2: probability to choose type 2
    :param lbd2: the lambda value of type 2's exponential distribution
           
    : return: generated value once
    """
    return st.rv_discrete(values=([st.expon.rvs(scale=1 / lbd1), st.expon.rvs(scale=1 / lbd2)], [p1, p2])).rvs(size=1)
>>>>>>> 0bdbf99b32f0434322007640ea3a5b096c03ff46:src/func_dist.py


def pareto(alpha, scale):
    """
    Generate x from pareto distribution
<<<<<<< HEAD:func_dist.py
        Built-in Python: pdf = f_{X}(x)=\left\{\begin{array}{ll}{\frac{\alpha x_{\mathrm{m}}^{\alpha}}{x^{\alpha+1}}} & {x \geq x_{\mathrm{m}}} \\ {0} & {x<x_{\mathrm{m}}}\end{array}\right.
                    mean = b * scale
=======
        Built-in Python: pdf = f_{X}(x)=\left\{\begin{array}{ll}{\frac{\alpha x_{\mathrm{m}}^{\alpha}}{x^{\alpha+1}}} &
                               {x \geq x_{\mathrm{m}}} \\ {0} & {x<x_{\mathrm{m}}}\end{array}\right.
>>>>>>> 0bdbf99b32f0434322007640ea3a5b096c03ff46:src/func_dist.py
    :param alpha: alpha
                    assume x_min^b = 1, use scale to assign different x_min
    :return: generated value once
    """
<<<<<<< HEAD:func_dist.py
    return st.pareto(b = alpha, scale = scale).rvs(size = 1)
=======
    return st.pareto(b=alpha).rvs(size=1)
>>>>>>> 0bdbf99b32f0434322007640ea3a5b096c03ff46:src/func_dist.py

