#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/05/16 10:02
# @File:    TEST.py

# @Content:

from __future__ import print_function
import tensorflow as tf
import numpy as np

sess = tf.InteractiveSession()


_X = np.array([[1,2,3], [4,5,6]])
X = tf.convert_to_tensor(_X)

out = tf.cumsum(X, axis=1)
print(out.eval())



