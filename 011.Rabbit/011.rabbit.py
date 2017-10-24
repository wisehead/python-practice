#############################################################
#   File Name: 011.rabbit.py
#     Autohor: Hui Chen (c) 2017
#        Mail: chenhui13@baidu.com
# Create Time: 2017/10/23-10:53:34
#############################################################
#!/usr/bin/env python 
#-*- coding:utf8 -*-
def Fab(inum):
    if inum < 0:
        return -1
    if inum == 0:
        return 0
    elif inum == 1:
        return 1
    else:
        return Fab(inum - 1) + Fab(inum - 2)

input_str = raw_input("please input num: ")
x = long(input_str)
for i in range(x):
    ret = Fab(i)
    print "Fab(%d) is: %d" % (i, ret)
