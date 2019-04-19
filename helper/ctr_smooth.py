#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/04/18 15:46
# @File:    ctr_smooth.py

# @Content:



def smooth_beyes(PV, CLICK, mean_ctr, M):
    '''
        当PV很小时, 只看点击率是没有用的

    :param PV:
    :param CLICK:
    :param mean_ctr: 所有样本的click总和 / 所有样本的pv总和
    :param M: PV平滑参数, 当PV远小于M时, 以均值mean_ctr为主, 当PV很大时, 以真实ctr为主
    :return:
    '''

    truth_ctr = CLICK * 1.0 / PV
    smooth_ctr = truth_ctr * (PV / (PV + M)) + mean_ctr * (M / (PV + M))
    return smooth_ctr


if __name__ == '__main__':
    print(smooth_beyes(10, 7, 0.5, 5))