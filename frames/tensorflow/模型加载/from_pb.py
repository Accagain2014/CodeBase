#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : from_pb.py
# Author            : chenmaosen <chenmaosen@360.cn>
# Date              : 09.12.2019
# Last Modified Date: 12.12.2019
# Last Modified By  : chenmaosen <chenmaosen@360.cn>
# encoding=utf-8


import tensorflow as tf
import numpy as np
import os


'''
    TF 1.12
'''

class Loc_Ner:

    def __init__(self, conf, device):
        self.conf = conf
        gpu_options = tf.GPUOptions(visible_device_list="{}".format(device))
        gpu_options.allow_growth = True
        self._init_data()
        pb_f = os.path.join(self.conf['dir_ner_model'], "ner_model.pb")
        graph = tf.Graph()
        with tf.gfile.GFile(pb_f, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
        with graph.as_default():
            self.input_ids_p = tf.placeholder(tf.int32, [self.conf['batch_size'], self.conf['max_seq_length']], name="input_ids")
            self.input_mask_p = tf.placeholder(tf.int32, [self.conf['batch_size'], self.conf['max_seq_length']], name="input_mask")
            tf.import_graph_def(graph_def, {'input_ids': self.input_ids_p, 'input_mask': self.input_mask_p})
            self.pred_ids = tf.import_graph_def(graph_def, name='', input_map={'input_ids': self.input_ids_p, 'input_mask': self.input_mask_p}, return_elements=['pred_ids:0'])
        graph.finalize()

        with graph.as_default():
            self.sess = tf.Session(graph=graph, config=tf.ConfigProto(gpu_options=gpu_options))


    def predict(self, sentence):
        res_final = {}
        input_ids, input_mask, segment_ids, label_ids, tokens = self.convert(sentence)
        feed_dict = {self.input_ids_p: input_ids, self.input_mask_p: input_mask}
        pred_ids_result = self.sess.run([self.pred_ids], feed_dict)
        #print(pred_ids_result)
        pred_label_result = self.convert_id_to_label(pred_ids_result[0][0], self.id2label)
        #print(pred_label_result)
        ner_jsn = self.strage_combined_link_org_loc(tokens, pred_label_result[0])
        #print(ner_jsn)
        res_final['res'], res_final['target'] = self.post_process(ner_jsn)

        res_final['ner'] = ner_jsn
        res_final['label'] = pred_label_result[0]
        res_final['token'] = tokens
        #print(json.dumps(res_final, ensure_ascii=False))
        return res_final
