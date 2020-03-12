#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/04/22 15:09
# @File:    ml_loss.py

# @Content:

import numpy as np


def softmax(X):
	exps = np.exp(X - np.max(X))
	return exps / np.sum(exps)


def cross_entropy(X, y, using_onehot=True):
	"""
	log_loss / cross_entropy / categorical_crossentropy
    X is the logits
    y is labels (num_examples, 1)
    	Note that y is not one-hot encoded vector.
    	It can be computed as y.argmax(axis=1) from one-hot encoded vectors of labels if required.
    """
	M = y.shape[0]
	if using_onehot :
		log_likelihood = -np.log(np.max(X * y, -1))
	else:
		log_likelihood = -np.log(X[range(M), y]) # 找到y对应的那个类别所对应的logit
	loss = np.sum(log_likelihood) / M
	return loss


def softmaxe_cross_entropy(X, y, using_onehot=True):
	X = softmax(X)
	return cross_entropy(X, y, using_onehot)


def huber_loss(pred, y, alpha):
	'''
		In statistics, the Huber loss is a loss function used in robust regression, that is less sensitive to outliers in data than the squared error loss.
		解决离群点问题
	:param logits:
	:param y:
		if pred < alpha:
			loss = 1/2 * (pred -y)^2
		else:
			loss = alpha * | pred -y | - 1/2 * alpha^2
	:return:
	'''

	pass


def hinge_loss(pred, y):
	'''

	:param pred: predict logits
	:param y: true label, +/-1
	l(y) = max(0, 1 - pred * y) # margin is 1
	:return:
	'''
	pass


if __name__ == '__main__':
	labels = np.array([
		[0, 1],
		[0, 1],
		[1, 0]
	])
	logits = np.array([
		[1.0/3, 2.0/3],
		[1.0/3, 2.0/3],
		[1.0/3, 2.0/3]
	])
	print(cross_entropy(logits, labels, True))