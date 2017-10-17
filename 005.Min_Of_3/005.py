#############################################################
#   File Name: 005.py
#     Autohor: Hui Chen (c) 2017
#        Mail: chenhui13@baidu.com
# Create Time: 2017/10/17-11:25:42
#############################################################
#!/usr/bin/env python 
#-*- coding:utf8 -*-
input_str = raw_input("please input x: ")
x = long(input_str)
input_str = raw_input("please input y: ")
y = long(input_str)
input_str = raw_input("please input z: ")
z = long(input_str)

min_num = 0
max_num = 0
if x > y:
	if z < y:
		print z, y, x
	else:
		if x > z: 
			print y, z, x 
		else:
			print y, x, z
else:
	if z < x:
		print z, x, y 
	else:
		if y > z: 
			print x, z, y 
		else:
			print x, y, z

