#!/usr/bin/env python
#coding=utf-8

# @Date:    2018/10/17 20:12
# @File:    ml_metrics.py.py

# @Content:
import numpy as np

def calc_auc(pred, true):
    '''

    :param pred: 预测情况
    :param true: 真实情况
    :thresholds: 抛开thresholds谈auc曲线没意义，正是有了thresholds才能引入那种渐变, pred是thresholds的函数
    :return:
    '''
    pred = np.array(pred)
    true = np.array(true)

    sort_index = np.argsort(pred)[::-1] # 从大到小
    true = true[sort_index]
    pred = pred[sort_index]

    auc, fps, tps, threshold = 0.0, [0.0], [0.0], [np.max(pred)+1e-3]
    for i in range(len(true)):
        tps.append(tps[-1] + true[i])
        fps.append(fps[-1] + 1.0-true[i])
        threshold.append(pred[i])
        auc += (fps[-1] - fps[-2])*(tps[-1] + tps[-2]) / 2

    auc = auc * 1.0 / fps[-1] / tps[-1]
    fps = np.array(fps) / fps[-1]
    tps = np.array(tps) / tps[-1]
    return auc, tps, fps, threshold

if __name__ == '__main__':
    pred = [0.1, 0.4, 0.35, 0.8]
    true = [0, 0, 1, 1]
    print calc_auc(pred, true)
