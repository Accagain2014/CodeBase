#!/usr/bin/env python
#coding=utf-8

# @Author:
# @Email:
# @Date:    2018/10/22 15:58
# @File:    args.py

# @Content: 处理python控制台参数样例

# import argparse
#
# parser = argparse.ArgumentParser(description="Args Summary Explanation.")
#
# parser.add_argument('-knn', type=argparse.FileType('r'), default=None)
# parser.add_argument('-id_title', type=argparse.FileType('r'), default=None)
# parser.add_argument('-output', type=argparse.FileType('w'), default=sys.stdout)
#
# args = parser.parse_args()


import argparse
arg_parser = argparse.ArgumentParser(description="svideo_log_stat")
arg_parser.add_argument("--log_mapper", action="store_true",
                        help="Extract necessary info from video_feedback log")
arg_parser.add_argument("--log_reducer", action="store_true",
                        help="Extract necessary info from video_feedback log")

arg_parser.add_argument("--today", type=str, default=None,
                        help="")
args = arg_parser.parse_args()

args.log_mapper = "dff"

print(args.log_mapper)
