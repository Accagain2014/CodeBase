#!/usr/bin/env python3
#coding=utf-8

'''
@Author : Accagain
@Time   : 2020/3/19 上午9:41
@File   : 2_plot_scatter_points.py

@Cont
    
'''

import matplotlib.pyplot as plt
import numpy as np


def plot_embeddings(M_reduced, word2Ind, words, save_path=None):
  """ Plot in a scatterplot the embeddings of the words specified in the list "words".
      NOTE: do not plot all the words listed in M_reduced / word2Ind.
      Include a label next to each point.

      Params:
          M_reduced (numpy matrix of shape (number of unique words in the corpus , 2)): matrix of 2-dimensioal word embeddings
          word2Ind (dict): dictionary that maps word to indices for matrix M
          words (list of strings): words whose embeddings we want to visualize
  """

  # ------------------
  # Write your implementation here.
  for word in words:
    word_id = word2Ind[word]
    x = M_reduced[word_id][0]
    y = M_reduced[word_id][1]
    plt.scatter(x, y, marker='x', color='red')
    plt.text(x + 0.001, y + 0.001, word, fontsize=9)

  if save_path:
    plt.savefig(save_path)
  plt.show()


if __name__ == '__main__':
  M_reduced_plot_test = np.array([[1, 1], [-1, -1], [1, -1], [-1, 1], [0, 0]])
  word2Ind_plot_test = {'test1': 0, 'test2': 1, 'test3': 2, 'test4': 3, 'test5': 4}
  words = ['test1', 'test2', 'test3', 'test4', 'test5']
  plot_embeddings(M_reduced_plot_test, word2Ind_plot_test, words, save_path="images/2_scatter_points.png")
