#############################################################
#   File Name: 008.multiply_table.py
#     Autohor: Hui Chen (c) 2017
#        Mail: chenhui13@baidu.com
# Create Time: 2017/10/23-10:20:19
#############################################################
#!/usr/bin/env python 
#-*- coding:utf8 -*-
from __future__ import print_function

for i in range(1,10):
	for j in  range(1,10):
		#print "%d*%d=%d" % (i, j, i*j)
		if j <= i:
			print("%d*%d=%d " % (i, j, i*j), end='')
		if j == 9:
			print("")
