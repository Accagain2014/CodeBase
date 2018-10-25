#coding=utf-8
from examples.NB_CL_Case.config import GlobalConfig as GC
from system.tools import Tools


class NaiveBayes(object):
	"""
		docstring for NaiveBayes
		adopt Laplace smoothing 
	"""
	def __init__(self):
		super(NaiveBayes, self).__init__()
		
	def train(self):
		self.trainDataFrame = Tools.readFromTable(GC.trainFile, names=['Y', 'A1', 'A2', 'A3', 'A4', 'A5'])
		#print self.trainDataFrame
		self.N = len(self.trainDataFrame)
		self.kinds = list(self.trainDataFrame['Y'].drop_duplicates().values)
		self.XColumns = filter(lambda x: x!='Y', self.trainDataFrame.columns)
		#print XColumns
		#XDataFrame = self.trainDataFrame[XColumns]
		#print XDataFrame

		self.pY = [(len(self.trainDataFrame[self.trainDataFrame.Y == kind])*1.0 +1)\
		/(self.N + len(self.kinds)) for kind in self.kinds]
		
		self.conditionP = {}
		for kind in self.kinds:
			self.conditionP[kind] = {}
			currentFrame = self.trainDataFrame[self.trainDataFrame.Y == kind]
			currentSum = len(currentFrame)

			for x in self.XColumns:
				self.conditionP[kind][x] = {}
				currentXKinds = list(self.trainDataFrame[x].drop_duplicates().values)
				for xKind in currentXKinds:
					self.conditionP[kind][x][xKind] = ((len(currentFrame[currentFrame[x] == xKind]))*1.0 + 1)\
					/(currentSum + len(currentXKinds))

		print self.conditionP
		print self.pY

	def predict(self):
		testDataFrame = Tools.readFromTable(GC.testFile, names=['Y', 'A1', 'A2', 'A3', 'A4', 'A5'])
		testDataFrame['predictY'] = 0
		testDataFrame['maxP'] = 0
		for index, row in testDataFrame.iterrows():
			resultC = 0
			resultP = 0
			for c in self.kinds:
				nowP = self.pY[self.kinds.index(c)]
				for x in self.XColumns:
					nowP *= self.conditionP[c][x][row[x]]
					if nowP > resultP:
						resultP = nowP
						resultC = c
			testDataFrame.loc[index, 'predictY'] = resultC
			testDataFrame.loc[index, 'maxP'] = resultP

		print 'Accuracy:' + str(len(testDataFrame[testDataFrame.predictY == testDataFrame.Y])\
			*1.0/(len(testDataFrame)))

		testDataFrame.to_csv(GC.resultFile, index=False) 
