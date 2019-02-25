# -*- coding: utf-8 -*-

"""
Example for Visual Bayesian Personalized Ranking
Data: http://jmcauley.ucsd.edu/data/tradesy/

@author: Quoc-Tuan Truong <tuantq.vnu@gmail.com>
"""

import cornac
from cornac.datasets import tradesy
from cornac.data import ImageModule
from cornac.eval_methods import RatioSplit


feedback = tradesy.load_data()
item_feature = tradesy.load_feature() # BIG file
item_image_module = ImageModule(id_feature=item_feature, normalized=True)

ratio_split = RatioSplit(data=feedback,
                         test_size=0.01,
                         rating_threshold=0.5,
                         exclude_unknowns=True,
                         verbose=True,
                         item_image=item_image_module)

vbpr = cornac.models.VBPR(k=10, k2=20, n_epochs=50, batch_size=100, learning_rate=0.005,
                          lambda_w=1, lambda_b=0.01, lambda_e=0.0, use_gpu=True)

auc = cornac.metrics.AUC()
rec_50 = cornac.metrics.Recall(k=50)

exp = cornac.Experiment(eval_method=ratio_split,
                        models=[vbpr],
                        metrics=[auc, rec_50])
exp.run()
