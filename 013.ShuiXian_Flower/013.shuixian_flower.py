#############################################################
#   File Name: 013.shuixian_flower.py
#     Autohor: Hui Chen (c) 2017
#        Mail: chenhui13@baidu.com
# Create Time: 2017/10/26-14:15:30
#############################################################
#!/usr/bin/env python 
#-*- coding:utf8 -*-
for i in range(100,1000):
	ge = i % 10
	shi = (i % 100)/10
	bai = i / 100
	x = ge*ge*bai + shi*shi*bai + bai*bai*bai
	#print "%d:%d, %d, %d: x is %d" % (i,bai, shi, ge, x)
	if (ge*ge*ge + shi*shi*shi + bai*bai*bai == i):
		print "%d:%d, %d, %d" % (i,bai, shi, ge)

