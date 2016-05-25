#coding=utf-8
import pandas as pd
import numpy as np
from config import GlobalConfig as GC
from helper import Tools
import math

class ChowLiu(object):
	"""docstring for Chow-Liu"""
	def __init__(self):
		super(ChowLiu, self).__init__()
	

	def calMI(self):
		dataFrame = Tools.readFromTable(GC.trainFile, names=['Y', 'A1', 'A2', 'A3', 'A4', 'A5'])
		self.XCloumns = filter(lambda x: x!='Y', dataFrame.columns)
		
		self.nodeEdges = [[] for i in self.XCloumns]
		N = len(dataFrame)
		#print XCloumns
		self.edges = []
		for i in range(len(self.XCloumns)):
			for j in range(i+1, len(self.XCloumns)):
				xiKinds = list(dataFrame[self.XCloumns[i]].drop_duplicates().values)
				xjKinds = list(dataFrame[self.XCloumns[j]].drop_duplicates().values)
				value = 0
				for iKind in xiKinds:
					for jKind in xjKinds:
						pxy = len(dataFrame[(dataFrame[self.XCloumns[i]] == iKind) \
						& dataFrame[self.XCloumns[j]] == jKind])*1.0 /N
						px = len(dataFrame[dataFrame[self.XCloumns[i]] == iKind])*1.0/N
						py = len(dataFrame[dataFrame[self.XCloumns[j]] == jKind])*1.0/N
						#print i, j, iKind, jKind, pxy,px,py,pxy/px/py
						value += pxy * math.log(pxy/px/py, 2.0)
				self.edges.append((i, j, value))
		#print self.edges

	def find(self, x):
		y = x
		while(self.father[x] != -1):
			x = self.father[x]

		while(y != x):
			temp = self.father[y]
			self.father[y] = x
			y = temp
		return x

	def kruskal(self):
		self.father = [-1 for i in self.XCloumns]
		self.edges.sort(key=lambda x: x[2], reverse=True)
		#print self.edges

		for oneEdge in self.edges:
			xF = self.find(oneEdge[0])
			yF = self.find(oneEdge[1])
			if xF != yF:
				self.father[xF] = yF
				self.nodeEdges[oneEdge[0]].append(oneEdge[1])
				self.nodeEdges[oneEdge[1]].append(oneEdge[0])
				print str(oneEdge[0])+'<->'+str(oneEdge[1])+':\t'+str(oneEdge[2])
		print self.nodeEdges


