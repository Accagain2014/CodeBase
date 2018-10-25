#!/usr/bin/env python
#coding=utf-8

# @Author:  Chen Maosen
# @Email:   chenmaosen@360.cn
# @Date:    2018/10/17 14:53
# @File:    tensorflow_examples.py

# @Content: Learning tensorflow from example codes

import tensorflow as tf
import numpy as np

def test_gather():
    '''
        测试提取函数
    :return:
    '''
    input = tf.constant([range(5),
                     np.array(range(5))+1,
                    np.array(range(5))+2])

    result_matrix = tf.gather(input, [[1, 2], [0, 1]])  # 先获取[1, 2]和[0, 1]的结果，然后再整体带入后面的矩阵中
    '''
        tf.gather(matrix, [1, 2])的结果记为matrix1 [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]],
        tf.gather(matrix, [0, 1])的结果记为matrix2 [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5]],
        所以tf.gather(matrix, [[1, 2], [0, 1]])的结果是[matrix1, matrix2]
    '''

    result_scalar = tf.gather(input, 0)
    result_vector = tf.gather(input, [1, 2, 1])

    sess = tf.Session()

    print sess.run(result_scalar)
    print '***'*10
    print sess.run(result_vector)
    print '***'*10
    print sess.run(result_matrix)

def test_matmul():
    '''
        test multi-dimensions matrix multiplication in tensorflow
    :return:
    '''
    input_2d_x = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
    input_2d_y = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])
    input_2d_z = tf.matmul(input_2d_x, input_2d_y)

    input_3d_x = tf.constant(np.arange(1, 13, dtype=np.int32),
                shape=[2, 2, 3])
    input_3d_y = tf.constant(np.arange(13, 25, dtype=np.int32),
                shape=[2, 3, 2])
    input_3d_z = tf.matmul(input_3d_x, input_3d_y)


    input_4d_x = tf.constant(np.arange(1, 13, dtype=np.int32), shape=[2, 3, 2, 1])
    input_4d_y = tf.constant(np.arange(13, 21, dtype=np.int32), shape=[2, 3, 1, 2])
    input_4d_z = tf.matmul(input_4d_x, input_4d_y)
    # 先算最后的两个矩阵相乘，2*1， 1*2， 然后依次带入到2*3中，得到2*3*2*2

    sess = tf.Session()
    print sess.run(input_2d_z)
    print '***' * 10
    print sess.run(input_3d_z)
    print "***" * 10
    print sess.run(input_4d_z)
    print tf.shape(input_4d_z)


if __name__ == '__main__':
    # test_gather()
    test_matmul()