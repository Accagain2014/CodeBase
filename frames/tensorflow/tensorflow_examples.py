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
    '''
        input = [ [0, 1, 2, 3, 4],
                  [1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 6]
                ]
    '''

    result_matrix = tf.gather(input, [[1, 2], [0, 1]], axis=0)  # 先获取[1, 2]和[0, 1]的结果，然后再整体带入后面的矩阵中
    '''
        tf.gather(matrix, [1, 2])的结果记为matrix1 [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]],
        tf.gather(matrix, [0, 1])的结果记为matrix2 [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5]],
        所以tf.gather(matrix, [[1, 2], [0, 1]])的结果是[matrix1, matrix2]
    '''

    result_scalar = tf.gather(input, 0)
    result_vector = tf.gather(input, [1, 2, 1])
    result_multidims_matrix = tf.gather(input, [[[1, 2]], [[0, 1]]], axis=1)

    sess = tf.Session()

    print sess.run(result_scalar)
    print '***'*10
    print sess.run(result_vector)
    print '***'*10
    print sess.run(result_matrix)
    print '***'*10
    print sess.run(result_multidims_matrix)

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
    input_4d_y = tf.constant(np.arange(13, 18, dtype=np.int32), shape=[2, 3, 1])
    input_4d_z = tf.matmul(input_4d_x, input_4d_y)
    # 先算最后的两个矩阵相乘，2*1， 1*2， 然后依次带入到2*3中，得到2*3*2*2

    sess = tf.Session()
    print sess.run(input_2d_z)
    print '***' * 10
    print sess.run(input_3d_z)
    print "***" * 10
    print sess.run(input_4d_z)
    print tf.shape(input_4d_z)

def test_tile():
    '''

    :return:
    '''
    T, N = 4, 3
    out = tf.tile(tf.expand_dims(tf.range(T), 0), [N, 1])
    sess = tf.Session()
    print sess.run(out)

def test_argmax():
    input = tf.constant([range(5),
                         np.array(range(5)) + 1,
                         np.array(range(5)) + 2])
    '''
        input = [ [0, 1, 2, 3, 4],
                  [1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 6]
                ]
    '''
    sess = tf.Session()
    print sess.run(tf.argmax(input, -1))

def sovle_problem_1():
    input = tf.constant([range(5),
                         np.array(range(5)) + 1,
                         np.array(range(5)) + 2])
    '''
        input = [ [0, 1, 2, 3, 4],
                  [1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 6]
                ]
    '''
    input = tf.constant([
        [0.99, 0.8, 0.7, 0.5, 0.5],
        [0.2, 0.3, 0.6, 0.7, 0.8],
        [0.1, 0.1, 0.1, 0.5, 1]
    ])
    sess = tf.Session()
    mask = tf.cast(tf.cast(tf.greater(input, 3), tf.int32), tf.float32)


    start_label = tf.constant(np.array([0, 2, 3]))
    start_label = tf.sequence_mask(start_label, 5, dtype=tf.int32) # not include the index

    end_label = tf.constant(np.array([2, 4, 3]))
    end_label = tf.sequence_mask(end_label+1, 5, dtype=tf.int32)

    res = end_label - start_label

    log_loss = tf.losses.log_loss(res, input)

    print sess.run([mask, start_label, end_label, res, log_loss])

def get_start_end_seq_mask(seq_len=5, length=3):
  '''

  :param seq_len: n_ctx
  :param length: ans_avg_len
  :return:
  '''
  s = tf.constant(np.array(range(seq_len)))  # [0, 1, ..., seq_len-1]
  s = tf.expand_dims(s, axis=-1)  # [[0], [1], ..., [seq_len-1]]
  s = tf.tile(s, [1, length])  # [[0, 0, 0], [1, 1, 1], ..., [seq_len-1, seq_len-1, seq_len-1]]
  s = tf.concat(tf.unstack(s, axis=0), axis=0)  # [0, 0, 0, 1, 1, 1, 2, 2, 2, ..., 4, 4, 4]

  gap = tf.constant(np.array(range(length)))  # [0, 1, 2]
  gap = tf.tile(gap, [seq_len])  # [0, 1, 2, 0, 1, 2, ..., 0, 1, 2]

  e = s + gap  # [0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4, 5,  ... ]
  s_mask = tf.cast(tf.sequence_mask(s+1, seq_len, dtype=tf.int32), tf.float32)  #
  s_mask_ = tf.cast(tf.sequence_mask(s, seq_len, dtype=tf.int32), tf.float32)
  s_mask = s_mask - s_mask_

  e_mask = tf.cast(tf.sequence_mask(e + 1, seq_len, dtype=tf.int32), tf.float32)
  e_mask_ = tf.cast(tf.sequence_mask(e, seq_len, dtype=tf.int32), tf.float32)
  e_mask = e_mask - e_mask_

  #res = e_mask - s_mask
  res = e_mask + s_mask
  res = res / tf.reduce_sum(res, axis=-1, keepdims=True)
  res = 2.0 * res
  return res

def losses():
    input = tf.constant(np.array([
            [0.5, 0.5, 0.5],
            [0.5, 0.5, 0.5]
            ]), dtype=tf.float32)
    label = tf.ones_like(input, dtype=tf.int32)
    label = tf.constant(np.array([
        [0, 0, 1],
        [0, 0, 1]
    ]), dtype=tf.int32)

    sess = tf.Session()
    #loss = tf.losses.log_loss(label, input)
    loss = tf.losses.softmax_cross_entropy(label, input)
    print sess.run([loss, input[1:, :]])

def sequence_product(seq, n_ctx=5, ans_avg_len=3, hidden_size=5):
    mask = tf.transpose(get_start_end_seq_mask(n_ctx, ans_avg_len))  # [seq_length * ans_avg_len, seq_length ] => [seq_length, seq_length * ans_avg_len]

    now_seq = tf.reshape(seq, [-1, n_ctx, hidden_size])  # [batch_size, seq_length, hidden_size]
    now_seq = tf.transpose(now_seq, perm=[0, 2, 1])  # [batch_size, hidden_size, seq_length]
    now_seq = tf.reshape(now_seq, [-1, n_ctx])  # [batch_size * hidden_size, seq_length]
    now_seq = tf.matmul(now_seq, mask)  # [batch_size*hidden_size, seq_length * ans_avg_len]
    now_seq = tf.reshape(now_seq, [-1, hidden_size, n_ctx * ans_avg_len])
    seq = tf.reshape(tf.transpose(now_seq, perm=[0, 2, 1]),
                     [-1, hidden_size])  # [batch_size * seq_length * ans_avg_len, hidden_size]

    return tf.reshape(seq, [-1, n_ctx*ans_avg_len, hidden_size])

def get_position_cross_clf_label(positions, seq_length, ans_avg_len):
  start_labels = tf.reshape(positions[:, 0], [-1])  # positions shape: [batch_size, 2] => [batch_size]
  end_labels = tf.reshape(positions[:, 1], [-1])
  ans_len = end_labels - start_labels +1  # [batch_size] # 超过ans_avg_len则为avg_len

  mask = tf.cast(tf.greater(ans_len, ans_avg_len), tf.int32) * (
            tf.zeros_like(ans_len, dtype=tf.int32) + ans_avg_len)

  ans_len = ans_len * (1 - tf.cast(tf.greater(ans_len, ans_avg_len), tf.int32)) + mask
  return start_labels * ans_avg_len + ans_len - 1


def metric():

    tf.metrics.accuracy(tf.ones_like(), ground_truth)


def test_boolean_mask():
    # 它会自动补充
    input = tf.constant([
        [0.99, 0.8, 0.7, 0.5, 0.5],
        [0.2, 0.3, 0.6, 0.7, 0.8],
        [0.1, 0.1, 0.1, 0.5, 1]
    ])

    mask = tf.constant([
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ])

    sess = tf.Session()
    print(sess.run(tf.boolean_mask(input, mask)))


def test():
    a = np.array([
       np.array(range(5))+0.0,
       np.array(range(5))+1.0,
       np.array(range(5))+2.0,
       np.array(range(5))+3.0,
       np.array(range(5))+4.0

    ])
    input = tf.constant(np.array([
        a, a+1, a+2, a+3
    ]), dtype=tf.float32) # 4 * 5 * 5

    # print(input.shape)

    input = tf.constant(np.array([
        [2, 3],
        [1, 1],
        [1, 4],
        [2, 2],
        [0, 0]
    ]), dtype=tf.int32)

    #output = sequence_product(input)
    output = get_position_cross_clf_label(input, 5, 20)
    output = get_start_end_seq_mask()
    #output = tf.argmax(input, axis=-1)[2]
    sess = tf.Session()
    print(sess.run(output))

def test_functions():
    a = np.array([
        np.array(range(5)) + 0.0,
        np.array(range(5)) + 1.0,
        np.array(range(5)) + 2.0,
        np.array(range(5)) + 3.0,
        np.array(range(5)) + 4.0

    ])

    a = tf.constant(a)

    sess = tf.Session()
    print(a.shape.ndims)
    print(a.shape.as_list())
    print(sess.run(tf.shape(a)))

if __name__ == '__main__':
    # test_gather()
    #test_matmul()
    # test_tile()
    # test_argmax()
    # sovle_problem_1()
    # solve_problem_2()
    # losses()
    # test()
    # test_boolean_mask()
    # test_gather()
    test_functions()