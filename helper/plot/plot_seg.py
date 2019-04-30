#!/usr/bin/env python
#coding=utf-8

# @Author:  Chen Maosen
# @Email:   chenmaosen@360.cn
# @Date:    2018/11/07 10:25
# @File:    plot_seg.py

# @Content: 一些工具函数

import numpy as np
import pandas as pd
import json
import math
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
  reload(sys)
  sys.setdefaultencoding(defaultencoding)

def cross_entropy(y_true, y_pred, epsilon=1e-15):
    '''

    :param y_true: 将完成度看成是推荐的概率
    :param y_pred: 预测推荐为1的概率
    :param epsilon: 精度
    :return: cross_entropy
    H(y_true, y_pred) = H(y_true) + DL(y_true, y_pred), 当y_true是[0, 1]时, H(y_true)=0,
    两个不同模型比较log loss意义不大？对排序来说，
    '''
    if np.max(y_pred) > 1:
        y_pred = y_pred / np.max(y_pred)
    N = y_true.shape[0]
    y_true = np.clip(y_true, epsilon, 1-epsilon)
    y_pred = np.clip(y_pred, epsilon, 1-epsilon)
    return - np.sum(np.sum(y_true * np.log(y_pred + epsilon))) / N


def read_from(filename):
    video_df = pd.read_csv(filename, encoding='utf-8', verbose=False, skip_blank_lines=False)
    video_df['share_success'] = video_df['share_success'].map(lambda x: int(str(x).strip()))
    if "\tvid" in list(video_df.columns):
        video_df.rename(columns={'\tvid': 'vid'}, inplace=True)
    video_df['vid'] = video_df['vid'].map(lambda x: str(x).strip())
    return video_df

def read_json(filename):
    with open(filename, "r") as fr:
        res = map(lambda x: json.loads(x.strip(), encoding="utf-8"), fr.readlines())
    return res

def _seg(x):
    if x > 10:
        x = 10.0
    return max(1.0, math.floor(x))


def show(ax, save_path=None, set_h=None):
    '''

    :param ax:
    :param save_path:
    :param set_h: [(y1, color1), (y2, color2), ...]
    :return:
    '''
    for p in ax.patches:
        hi = float(p.get_height())
        if hi >= 1:
            hi = int(hi)
        ax.annotate(str(hi), (p.get_x() , p.get_height() * 1.0), fontSize="x-small")
    if not save_path is None:
        plt.savefig(save_path)
    if set_h:
        for one_horizon_line in set_h:
            ax.axhline(y=one_horizon_line[0], color=one_horizon_line[1])

    plt.show()
    plt.close()


def sort_by(df, columns=[], ascending=[], out_columns=None):
    sort_result = df.sort_values(by=columns, ascending=ascending)
    if out_columns is None:
        return sort_result
    return sort_result[out_columns]

def seg_stat(df, column, function, stat_key='vid', save_path=[None, None]):
    '''
    对column分段后，在stat_key上计数和求和统计画图，横坐标：column分段区间, 纵坐标：stat_key在该区间上的统计分析
    :param df: 原始df
    :param column: 对该列进行统计分析
    :param function: 对column的分段
    :param stat_key: 对column分段后的统计的字段
    :param save_path:
    :return:
    '''
    new_column = column+"_seg"
    df[new_column] = df[column].map(function)
    group_vid = df.groupby([new_column])[stat_key].count()
    title = stat_key + ":" + column+" seg count distribution"
    figsize=(8, 7)
    show(group_vid.plot(kind="bar", grid=True, title=title, figsize=figsize), save_path=save_path[0])

    group_column_vid = pd.DataFrame(group_vid)
    sum = group_column_vid[stat_key].sum()
    group_column_vid['rate'] = group_column_vid[stat_key].map(lambda x: round(x * 1.0 / sum, 2))
    group_column_vid.reset_index(inplace=True)
    title = stat_key + ":" + column+" seg rate distribution"

    show(group_column_vid.plot(x=new_column, y='rate', kind="bar", grid=True, title=title, figsize=figsize), save_path=save_path[1])


def degree_seg(x):
    if x == 0:
        return "0%~0%"
    floor = int(math.floor(x * 10))
    ceil = min(10, floor + 1)
    return "%s.%d%%~%d%%" % (chr(ord('a')+floor), floor*10, ceil*10)

def vlen_seg(x):
    if x >= 200:
        return "a. 200s"
    if x >= 100:
        return "b. 100-200s"
    if x >= 80:
        return "c. 80-100s"
    if x >= 60:
        return "d. 60-80s"
    if x >= 40:
        return "e. 40-60s"
    if x >= 20:
        return "f. 20-40s"
    if x >= 10:
        return "g. 10-20s"
    if x > 0:
        return "h. >0-10s"
    return "i. 0s"

def watch_times_seg(x):
    if x >= 1000:
        return "a. >=1000"
    if x >= 500:
        return "b. >=500"
    if x >= 100:
        return "c. >=100"
    if x >= 50:
        return "d. >=50"
    if x >= 40:
        return "e. >=40"
    if x >= 30:
        return "f. >=30"
    if x >= 20:
        return "g. >==20"
    if x >= 10:
        return "h. >=10"
    return "%s. =%d" % (chr(ord('h') + 10-int(x)), int(x))

def seg_two_column_stat(df, column, function, y_column="v_watch_degree", flag=0, save_path=None):
    '''
        column分段后, 对y_column的聚集统计（包括计数/求和/求平均）
    :param df:
    :param column:
    :param function:
    :param y_column:
    :param mean_count: 0 mean, 1 count, 2 sum
    :return:
    '''
    new_column = column+"_seg"
    figsize=(10, 9)
    df[new_column] = df[column].map(function)
    if flag == 0:
        group_vid = df.groupby([new_column])[y_column].mean().round(2)
        show(group_vid.plot(kind="bar", grid=True, title=column+" avg " + y_column + " distribution", figsize=figsize), save_path=save_path)
    elif flag == 1:
        group_vid = df.groupby([new_column])[y_column].count()
        show(group_vid.plot(kind="bar", grid=True, title=column + " count " + y_column + " distribution", figsize=figsize), save_path=save_path)
    elif flag == 2:
        group_vid = df.groupby([new_column])[y_column].sum()
        show(group_vid.plot(kind="bar", grid=True, title=column + " sum " + y_column + " distribution", figsize=figsize), save_path=save_path)

def write_data_to_file(filename, data):
    with open(filename, "w") as fw:
        fw.write(data)

