#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/04/27 17:13
# @File:    1_plot_confusion_matrix.py

# @Content:

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np


def plot_confusion_matrix(cls_true, cls_pred, num_classes, save_path=None):
	# This is called from print_test_accuracy() below.

	# cls_pred is an array of the predicted class-number for
	# all images in the test-set.


	# Get the confusion matrix using sklearn.
	cm = confusion_matrix(y_true=cls_true,
						  y_pred=cls_pred)

	# Print the confusion matrix as text.
	print(cm)

	# Plot the confusion matrix as an image.
	plt.matshow(cm)

	# Make various adjustments to the plot.
	plt.colorbar()
	tick_marks = np.arange(num_classes)
	plt.xticks(tick_marks, range(num_classes))
	plt.yticks(tick_marks, range(num_classes))
	plt.xlabel('Predicted')
	plt.ylabel('True')

	# Ensure the plot is shown correctly with multiple plots
	# in a single Notebook cell.
	if save_path:
		plt.savefig(save_path)
	plt.show()


if __name__ == '__main__':
	cls_true = np.array([1, 3, 2, 2, 1, 0, 3])
	cls_pred = np.array([1, 2, 2, 2, 3, 0, 1])
	num_classes = 4
	plot_confusion_matrix(cls_true, cls_pred, num_classes, save_path="images/1_confusion_matrix.png")