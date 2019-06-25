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


def parse_args():
  parser = argparse.ArgumentParser(description='tokenized desc')
  parser.add_argument('--tag_path', help='tag path', type=str)
  parser.add_argument('--src_path', help='src path', type=str)
  parser.add_argument('--dst_path', help='dst path', type=str)
  args = parser.parse_args()
  log.info(args)
  return args
