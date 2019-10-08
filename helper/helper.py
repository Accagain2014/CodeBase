#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/08/22 16:19
# @File:    helper.py

# @Content:

import hashlib


def f_format(x):
	### format digital data with leading zeros
	print("{:02d}".format(x))


def get_md5(text):
    return hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()


