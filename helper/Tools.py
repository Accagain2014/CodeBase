#coding=utf-8

import pandas as pd
import numpy as np

def readFromTable(fileName, names=None):
	return pd.read_table(fileName, sep=' ', index_col=False, header=None, names=names)
