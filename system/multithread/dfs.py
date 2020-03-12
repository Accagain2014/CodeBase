#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/03/12 10:38
# @File:    dfs.py

# @Content:

import copy
all_choices = []

def _dfs(model_index, models, choices, now_model_nums, ensemble_nums):
    if now_model_nums > ensemble_nums:
        return
    if model_index >= len(models):
        all_choices.append(choices)
        return
    for i in range(len(models[model_index])):
        choices.append(i)
        now_choices = copy.deepcopy(choices)
        _dfs(model_index + 1, models, now_choices, now_model_nums if i == 0 else now_model_nums+1, ensemble_nums)
        choices = choices[:-1]


if __name__ == '__main__':
    models = [[0, 1, 2, 3], [2, 3], [0, 2]]
    _dfs(0, models, [], 0, 2)
    for idx, one_choice in enumerate(all_choices):
        print(idx, one_choice)



