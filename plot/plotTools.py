#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

def plotGraph(x, labels):
	plt.figure(2, figsize=(8,8))
	ax = plt.subplot(111)
	bbox_props = dict(boxstyle="circle", fc='y', ec="0.1", alpha=0.9)
	vis = [False for i in x]
	
	
	def dfs(now, posX, posY):
		'''
		ax.text(-2, -2, "Sample A", ha="center", va="center", size=10,
        bbox=bbox_props)

        ax.annotate("",
            xy=(0.2, 0.2),
            xytext=(0.8, 0.8),
            arrowprops=dict(arrowstyle="->")
            )
		'''
		ax.text(posX, posY, labels[now], ha='center', va='center', size=15, bbox=bbox_props)
		vis[now] = True

		cnt = 0
		for i in x[now]:
			if vis[i]:
				continue
			cnt += 1
			ax.annotate("",xytext=(posX, posY),xy=(posX-2+cnt, posY-1),arrowprops=dict(arrowstyle="-"))
			dfs(i, posX-(2-cnt), posY-1)
	dfs(0, 0, 3)

	ax.set_xlim(-4, 2)
	ax.set_ylim(-1, 4)

	plt.show()
	pass

def plotCurve():
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
		y = map(lambda x: 1.0-pow((1-pow(x, r[i])), b[i]), s)
		print y
		#ax = plt.subplot(int('31'+str(i+1)))
		ax.plot(s, y, lineKind[i], label=labelKind[i])
	plt.legend(loc=4)
	plt.savefig('S-curve.png')
	plt.show()


if __name__ == '__main__':
	#plotGraph([[3], [3], [3, 4], [0, 2, 1], [2]], ['A'+str(i+1) for i in range(5)])
	
	plotCurve()


