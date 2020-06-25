# setup File for Levy Process
# author: Edward J. Xu
# date: 190620

import random
import pandas as pd
import numpy as np
import time
from numbers import Number
import logging
import scipy.stats as st


class LevyProcess():

    def __init__(self, mu:float, sigma:float, lbd:float, f_y):
        if sigma < 0:
            raise ValueError("The Gaussian intensity of a Levy process must "
                "be equal or greater than 0.")
        elif not callable(f_y):
            raise ValueError("Function to simulate inter-jump times.")

        self.mu = mu # linear drift
        self.sigma = sigma # Gaussian intensity
        self.lbd = lbd
        self.f_y = f_y

        self.phi1 = - mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 +
            2 * lbd / sigma ** 2)
        self.phi2 = mu / sigma ** 2 + np.sqrt(mu ** 2 / sigma ** 4 +
            2 * lbd / sigma ** 2)

    def update(self, pre:dict):
        """
        Update the value of v, w, p, a, m
        """
        i = random.expovariate(self.lbd)  # inter-arrival times
        s = pre["s"] + i
        y = self.f_y()

        v = random.expovariate(self.phi1)  # st.expon(scale=1 / phi1).rvs(size=1)[0]
        w = random.expovariate(self.phi2)  # st.expon(scale=1 / phi2).rvs(size=1)[0]
        p = pre["a"] + (v - w)
        a = pre["a"] + (v - w) + y
        m = max(pre["m"], pre["a"] + v, a)

        return {"v": v, "w": w, "p": p, "a": a, "m": m, "y": y, "s": s, "i": i}

    def realise(self, n_sample:int) -> pandas.core.frame.DataFrame:
        results = {0: {"v": 0, "w": 0, "p": 0, "a": 0, "m": 0,
            "y": self.f_y(), "s": 0, "i": 0}}

        for i in range(1, n_sample):
            results[i] = update(results[i-1])

        # p_result = list_p[-1]
        # a_result = list_a[-1]
        # m_result = list_m[-1]

        return pd.DataFrame.from_dict(results, orient='index')

    def sim(self, n_sim:int, n_sample:int) -> dict:
        results = {}

        time_start = time.time()
        for i in range(1: n_sim+1):
            results[i] = self.realise(n_sample)
        time_elapse = time.time() - time_start
        print(f"Time elapsed = {time_elapse} ;")

        return results

    @staticmethod
    def cal_fpp(results:dict, level:float) -> float:
        """
        Calculate first passage probability given the simulation result from
            `LevyProcess.sim()` and `level`.

        Argument
        ========
        results: dict of pandas dataframes with same number of samples
        level: the value to compare
        """
        n_sim = len(results)
        n_sample = results[0].shape[0]
        for i in range(n_sim):
            if results[i].shape[0] != n_sample
                raise ValueError("Number of samples are different.")

        ## Obtain all final `m`s from `results`.
        ms = [i.loc[n_sample - 1]["m"] for i in list(results.values())]

        fpp = sum([i > level for i in ms]) / n_sim
        return fpp
