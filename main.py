#coding=utf-8
from algorithms import NaiveBayes as NB

if __name__ == '__main__':
	classfier = NB.NaiveBayes()
	classfier.train()
	classfier.predict()