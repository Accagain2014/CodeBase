#!/usr/bin/env python3
#coding=utf-8

'''
@Author : Accagain
@Time   : 2020/3/27 下午10:15
@File   : hooks.py

@Cont
    
'''


class EvalHooks(tf.train.SessionRunHook):

  def __init__(self):
    pass

  def begin(self):
    self.valid_user = 0.0

    self.ndcg_1 = 0.0
    self.hit_1 = 0.0
    self.ndcg_5 = 0.0

  def end(self, session):
    print(
      "ndcg@1:{}, hit@1:{}， ndcg@5:{}, hit@5:{}, ndcg@10:{}, hit@10:{}, ap:{}, valid_user:{}".
        format(self.ndcg_1 / self.valid_user, self.hit_1 / self.valid_user,
               self.ndcg_5 / self.valid_user, self.hit_5 / self.valid_user,
               self.ndcg_10 / self.valid_user,
               self.hit_10 / self.valid_user, self.ap / self.valid_user,
               self.valid_user))

    def before_run(self, run_context):
      # tf.logging.info('run before run')
      # print('run before_run')
      variables = tf.get_collection('eval_sp')
      return tf.train.SessionRunArgs(variables)

    def after_run(self, run_context, run_values):
      # tf.logging.info('run after run')
      # print('run after run')
      masked_lm_log_probs, input_ids, masked_lm_ids, info = run_values.results
      masked_lm_log_probs = masked_lm_log_probs.reshape(
        (-1, FLAGS.max_predictions_per_seq, masked_lm_log_probs.shape[1]))


estimator.evaluate(
        input_fn=eval_input_fn,
        steps=None,
        hooks=[EvalHooks()])

