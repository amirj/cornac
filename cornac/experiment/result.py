# -*- coding: utf-8 -*-

"""
@author: Aghiles Salah <asalah@smu.edu.sg>
"""

import numpy as np
import pandas as pd


class SingleModelResult:
    """ Result class for a single model

    Parameters
    ----------
    """

    def __init__(self, metric_avg_results, metric_user_results = None):
        self.avg = metric_avg_results
        self.per_user = metric_user_results

    def _organize_avg_res(self, model_name, metric_names):
        self.avg = [self.metric_avg.get(mt_name, np.nan) for mt_name in metric_names]
        self.avg = np.asarray(self.avg)
        self.avg = self.avg.reshape(1,len(metric_names))
        self.avg = pd.DataFrame(data= self.avg, index=model_name, columns= metric_names)




class Result:
    """ Result Class

    Parameters
    ----------
    """
    def __init__(self, per_model_results = {}, avg_results = []):
        #self.per_model = per_model_results
        self.avg = avg_results
        self.verbose = verbose
        self.per_user = {}


    def _add_model_res(self, res, model_name):
        #self.per_model[model_name] = res
        self.avg.append(res.avg)
        self.per_user[model_name] = res.per_user[model_name]

    def show(self):
        print(self.avg)
