#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/03/11 19:15
# @File:    multithreads_findmax.py

# @Content: Use multi threads to find max element in long array.


from multiprocessing import Pool
import multiprocessing
import time
import math
import uuid
from itertools import  product
from functools import partial


def _find_max(sub_input, idx):
    res = -10000
    uid = str(uuid.uuid4()).split('-')[0]
    print("execute for {}. idx: {}, sleep 5s".format(uid, idx, sub_input))
    time.sleep(5)
    for i in sub_input:
        res = max(res, i)
    return (uid, res)

def multithreads_findmax(input=[2, 43, 3, -1, 0, 100], cpus=multiprocessing.cpu_count()):
    lenth = len(input)
    split_inputs_start = range(0, lenth, math.ceil(lenth/cpus))
    split_inputs_end = [_+math.ceil(lenth/cpus) for _ in split_inputs_start]
    split_inputs = [input[start:end] for (start, end) in zip(split_inputs_start, split_inputs_end)]

    print("all split inputs: {}".format(split_inputs))
    pool = Pool()
    res = pool.map(partial(_find_max, idx="1"), split_inputs) # 传参数
    print(res)


if __name__ == '__main__':
    multithreads_findmax(range(1001))