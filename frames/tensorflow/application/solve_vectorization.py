#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/02/28 14:28
# @File:    solve_vectorization.py

# @Content: solve problems proposed in vectorization.md

import tensorflow as tf

def solve_problems_4(rand_neg_num=2, max_ans_len=2, max_seq_len=3, margin=0.01):

    logits = tf.constant([
        [0.9, 0.2, 0.3, 0.4, 0.5, 0.7],
        [0.4, 0.1, 0.5, 0.2, 0.3, 0.8]
    ])

    lables = tf.constant([
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 1]
    ])

    batch_size = tf.shape(logits)[0]
    # 得到随机开始位置
    random_neg_start = tf.random_uniform([batch_size, max_ans_len * max_seq_len * rand_neg_num], minval=0, maxval=max_seq_len, seed=0, dtype=tf.int32)
    # 随机长度
    random_neg_len = tf.random_uniform([batch_size, max_ans_len * max_seq_len * rand_neg_num], minval=0, maxval=max_ans_len, seed=0, dtype=tf.int32)
    # 随机se
    random_neg_indices_org = tf.expand_dims(random_neg_start * max_ans_len + random_neg_len, -1)

    now_indices = tf.expand_dims(tf.tile(tf.expand_dims(tf.range(batch_size), -1), [1, max_seq_len * max_ans_len * rand_neg_num]), -1)
    random_neg_indices = tf.concat([now_indices, random_neg_indices_org], -1)
    neg_logits = tf.gather_nd(logits, random_neg_indices)  # 通过gather_nd构造索引
    neg_logits = tf.reshape(neg_logits, [batch_size, max_ans_len * max_seq_len, -1])


    expand_lables = tf.tile(tf.expand_dims(lables, -1), [1, 1, rand_neg_num])
    expand_logits = tf.tile(tf.expand_dims(logits, -1), [1, 1, rand_neg_num])
    pos_logits = expand_logits * tf.cast(expand_lables, tf.float32)
    neg_logits = neg_logits * tf.cast(expand_lables, tf.float32) + tf.cast(1 - expand_lables, tf.float32) * -margin

    temp = neg_logits - pos_logits + margin

    loss = tf.reduce_sum(tf.maximum(0.0, neg_logits - pos_logits + margin)) / tf.cast(batch_size, tf.float32)


    #pos_indices = tf.where(tf.equal(lables, 1))

    #expand_lables = tf.tile(tf.expand_dims(lables, axis=-1), [1, 1, 5])

    sess = tf.Session()
    # print(sess.run(now_indices))
    # print(sess.run(random_neg_indices_org))
    # print(sess.run(tf.concat([now_indices, random_neg_indices_org], axis=-1)))
    # print(sess.run(random_neg_indices))
    #print(sess.run(loss))
    print(sess.run(temp))
    #print(sess.run(expand_lables))


def test_concat():
    a = tf.constant([[[0], [0]], [[1], [1]]])

    b = tf.constant([[[1], [3]], [[4], [5]]])
    ab2 = tf.concat([a, b], axis=-1)

    sess = tf.Session()
    print(sess.run(ab2))



def solve_problem_6(topk=3):
    '''
        logits = [
            [0.9, 0.2, 0.3],
            [0.4, 0.1, 0.5]
        ]
        lables = [
            [1, 1, 0],
            [1, 0, 0]
        ]
    top_1_recall = (1/2 + 0)/2 = 0.15, top_2_recall = (1/2 + 1/1)/2 = 0.75, top_3_recall = (2/2 + 1/1)/2 = 1
    top_1_precise = (1/1 + 0/1)/2 = 0.5, top_2_precise = (1/2 + 1/2)/2 = 0.5 top_3_precise = (2/3 + 1/3)/2 = 0.5
    '''

    logits = tf.constant([
        [0.9, 0.2, 0.3],
        [0.4, 0.1, 0.5]
    ])
    lables = tf.constant([
        [1, 1, 0],
        [1, 0, 0]
    ])

    batch_size = tf.shape(logits)[0]
    label_num = tf.shape(logits)[1]
    valuese, indices = tf.nn.top_k(logits, label_num)


    now_indices = tf.expand_dims(
        tf.tile(tf.expand_dims(tf.range(batch_size), -1), [1, label_num]), -1)
    indices = tf.expand_dims(indices, -1)

    now_indices = tf.concat([now_indices, indices], -1)
    top_labels = tf.gather_nd(lables, now_indices)

    for topi in range(1, topk+1):
        precise = tf.metrics.accuracy(top_labels[:, :topi], tf.ones_like(top_labels[:, :topi]))
        recall = tf.metrics.recall(top_labels, tf.concat(
            [top_labels[:, :topi], tf.zeros([batch_size, label_num - topi], dtype=tf.int32)], axis=-1))


    with tf.Session() as sess:
        init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
        sess.run(init)
        print(sess.run(precise[1]))
        print(sess.run(recall[1]))


if __name__ == '__main__':
    #solve_problems_4()
    solve_problem_6()
    #test_concat()



