#############################################################
#   File Name: 010.time.py
#     Autohor: Hui Chen (c) 2017
#        Mail: chenhui13@baidu.com
# Create Time: 2017/10/23-10:45:02
#############################################################
#!/usr/bin/env python 
#-*- coding:utf8 -*-
import time
for i in range(100):
	time.sleep(1)
	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

