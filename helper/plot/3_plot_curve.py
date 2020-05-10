#!/usr/bin/env python3
#coding=utf-8

'''
@Author : Accagain
@Time   : 2020/3/19 上午9:54
@File   : 3_plot_curve.py

@Cont
    
'''


import matplotlib.pyplot as plt
import numpy as np


def plotCurve(save_path=None):
  '''
  plt.subplot(223) 表示创建2*2的四块画布,当前在第3块里面
  '''

  '''
  plot 1-(1-s^r)^b
  with different r and b
  '''
  plt.figure(figsize=(8, 4))
  s = np.arange(0.1, 1, 0.1)

  r = [3, 6, 5]
  b = [10, 20, 50]
  lineKind = ['k', 'r--', 'b--']
  labelKind = ['r=3,b=10', 'r=6,b=20', 'r=5,b=50']

  ax = plt.subplot(111)
  for i in range(len(r)):
    y = list(map(lambda x: 1.0 - pow((1 - pow(x, r[i])), b[i]), s))
    print(y)
    # ax = plt.subplot(int('31'+str(i+1)))
    ax.plot(s, y, lineKind[i], label=labelKind[i])
  plt.legend(loc=4)
  if save_path:
    plt.savefig(save_path)
  plt.show()


if __name__ == '__main__':
  plotCurve(save_path="images/3_curve.png")