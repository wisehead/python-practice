#############################################################
#   File Name: 005.std_answer.py
#     Autohor: Hui Chen (c) 2017
#        Mail: chenhui13@baidu.com
# Create Time: 2017/10/17-11:36:50
#############################################################
#!/usr/bin/env python 
#-*- coding:utf8 -*-
l = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l
