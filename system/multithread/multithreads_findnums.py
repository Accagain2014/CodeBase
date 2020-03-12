#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/05/28 17:04
# @File:    multithreads_findnums.py

# @Content:
'''
	Given a 2D matrix (or list of lists), count how many numbers are present between a given range in each row. We will work on the list prepared below.

'''

import numpy as np
from time import time
import multiprocessing as mp



def get_data():
	np.random.RandomState(100)
	arr = np.random.randint(0, 10, size=[2000000, 5])
	data = arr.tolist()
	print(data[:5])
	return data


def howmany_within_range(row, minimum=4, maximum=8):
	"""Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
	count = 0
	for n in row:
		if minimum <= n <= maximum:
			count = count + 1
	return count

def howmany_within_range_2(i, row, minimum=4, maximum=8):
	"""Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
	count = 0
	for n in row:
		if minimum <= n <= maximum:
			count = count + 1
	return (i, count)


def test_brute_solution(data):
	now_time = time()
	results = []
	for row in data:
		results.append(howmany_within_range(row, minimum=4, maximum=8))
	print(results[:10])
	print("execute time: {}s".format((float(time())-float(now_time))))

def test_multi_apply(data):
	now_time = time()
	pool = mp.Pool(mp.cpu_count())
	results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]
	pool.close()
	print(results[:10])
	print("execute time: {}s".format((float(time())-float(now_time))))


def test_multi_map(data):
	#data = get_data()
	now_time = time()
	pool = mp.Pool(mp.cpu_count())
	results = pool.map(howmany_within_range, [row for row in data])
	pool.close()
	print(results[:10])
	print("execute time: {}s".format((float(time())-float(now_time))))

def test_multi_startmap(data):
	now_time = time()
	pool = mp.Pool(mp.cpu_count())
	results = pool.starmap(howmany_within_range, [(row, 4, 8) for row in data])
	pool.close()
	print(results[:10])
	print("execute time: {}s".format((float(time())-float(now_time))))



def test_proc_apply(data):
	now_time = time()
	pool = mp.Pool(mp.cpu_count())
	results = []
	def _collect_result(result):
		results.append(result)
	for i, row in enumerate(data):
		pool.apply_async(howmany_within_range_2, args=(i, row, 4, 8), callback=_collect_result)
	pool.close()
	pool.join()
	results.sort(key=lambda x: x[0])
	results = [ r for i, r in results]
	print(results[:10])
	print("execute time: {}s".format((float(time())-float(now_time))))



if __name__ == '__main__':
	data = get_data()
	test_brute_solution(data)
	#test_multi_apply(data)
	test_multi_map(data)
	#test_multi_startmap(data)
	test_proc_apply(data)