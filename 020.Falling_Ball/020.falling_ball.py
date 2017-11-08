#!/usr/bin/env python 
#-*- coding:utf8 -*-
'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
count = 100.0
high = 100.0
for i in range(1,11):
	high = high / 2
	count += high*2
	print "%d:	height is: %f, count is:%f " % (i, high, count)


