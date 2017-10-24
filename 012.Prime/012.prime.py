#############################################################
#   File Name: 012.prime.py
#     Autohor: Hui Chen (c) 2017
#        Mail: chenhui13@baidu.com
# Create Time: 2017/10/24-10:29:35
#############################################################
#!/usr/bin/env python 
#-*- coding:utf8 -*-
import math
not_prime = 0
for i in range(101,200):
	for j in range(2, int(math.sqrt(i))+1):
		if i%j == 0:
			not_prime = 1
			break
	if not_prime == 0:
		print i
	not_prime = 0
