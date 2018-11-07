#!/usr/bin/env python
#coding=utf-8

# @Author:  Chen Maosen
# @Email:   chenmaosen@360.cn
# @Date:    2018/10/22 15:58
# @File:    args.py

# @Content: 处理python控制台参数样例

import argparse

parser = argparse.ArgumentParser(description="Args Summary Explanation.")

parser.add_argument('-knn', type=argparse.FileType('r'), default=None)
parser.add_argument('-id_title', type=argparse.FileType('r'), default=None)
parser.add_argument('-output', type=argparse.FileType('w'), default=sys.stdout)

args = parser.parse_args()