#coding=utf-8

import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

'''
	Handle continus features and discrete features.
	Do buckets/bins/hash operation for continus features.
	Do one hot operation for discrete features.
	XGB2onehot
'''

def xgb2csr(model, trainX, X):
    '''
        use xgb model to generate one hot feature for other model, like LogisticRegression Mdoel.

    :param model:
    :param trainX:
    :param X:
    :return:
    '''

    ret_indexs = model.apply(X)
    ret_indexs_leaves = model.apply(trainX)

    print('Begin')
    n_estimators = len(ret_indexs[0])
    n_samples = len(ret_indexs)
    row_index = np.zeros(n_samples * n_estimators)
    col_index = np.zeros(n_samples * n_estimators)
    data = np.zeros(n_samples * n_estimators)
    idx = 0
    sum = 0
    for j in range(n_estimators):
        for i in range(n_samples):
            row_index[idx] = i
            col_index[idx] = sum + ret_indexs[i][j]
            data[idx] = 1
            idx += 1
        sum += len(set([ret_indexs_leaves[i][j] for i in range(n_samples)]))
        pass
    print('Done')
    return csr_matrix((data, (row_index, col_index)))

