#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/10/16 09:50
# @File:    useful_code.py

# @Content:


'''
	解决 requests Max retries exceeded
'''

s = requests.session()
s.keep_alive = False



'''
	Code
'''

import pathos.pools as pp
from functools import partial


pool = pp.ProcessPool(8)
pool.map(partial(func, func_arg1=arg1, func_arg2=arg2), data)
pool.close()
