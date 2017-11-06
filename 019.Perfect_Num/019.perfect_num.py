#!/usr/bin/env python 
#-*- coding:utf8 -*-
'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''
for i in range(1,1000):
	list1=[]
	temp = i
	count = 0
	for x in range(1,i):
		if temp % x == 0:
			list1.append(x)
			count += x
	if count == i:
		print i 
		print list1

