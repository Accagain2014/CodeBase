#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/06/13 14:22
# @File:    log.py

# @Content:


import logging as log
log.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                level=log.INFO)


attrs = vars(CLASS_INSTANCE)
  for ele in attrs.items():
    log.info('{}\t{}'.format(ele[0], ele[1]))


