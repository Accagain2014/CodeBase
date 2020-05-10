#!/usr/bin/env python3
#coding=utf-8

'''
@Author : Accagain
@Time   : 2020/4/2 下午6:36
@File   : from_ckpt.py

@Cont
    
'''

import tensorflow as tf


class Online_NER:

  def __init__(self, bert_config, f, device):
    self.config = bert_config

    now_gpu = device

    gpu_options = tf.GPUOptions(visible_device_list="{}".format(now_gpu))

    gpu_options.allow_growth = True
    self.sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
    self.input_ids = tf.placeholder(tf.int32, shape=[None, 512])
    self.input_mask = tf.placeholder(tf.int32, shape=[None, 512])
    self.segment_ids = tf.placeholder(tf.int32, shape=[None, 512])
    features_place = {'input_ids': self.input_ids, 'input_mask': self.input_mask, 'segment_ids': self.segment_ids}
    ner_model = Model(**self.config)
    _, _, self.pred_op = ner_model.model(features_place, None, tf.estimator.ModeKeys.PREDICT) # 建图的过程, 把predict_op拿到
    with self.sess.graph.as_default():
      saver = tf.train.Saver()
      saver.restore(self.sess, f)


