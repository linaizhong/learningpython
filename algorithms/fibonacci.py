# -*- coding: utf-8 -*-
"""Algoritmos de Fibonacci"""

def iterative_fibonacci(num):
	if num <=0:
		return 0
	temp, result = 1, 1
	for i in xrange(3, num+1):
		temp, result = result, result + temp
	print result

def recursive_fibonacci(num):
	if num<=0:
		return 0
	elif num<=2:
		return 1
	else:
		return recursive_fibonacci(num-1) + recursive_fibonacci(num-2)

