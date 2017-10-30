#!/usr/bin/env python 
#-*- coding:utf8 -*-
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
'''
str_input = raw_input("please input a string: ")
count_alpha = 0
count_digit = 0
count_space = 0
count_else = 0
len_str = len(str_input) 

for c in str_input:
	if c.isdigit():
		count_digit += 1
	elif c.isalpha():
		count_alpha += 1
	elif c.isspace():
		count_space += 1
	else:
		count_else += 1
print "total length is: %d" % len_str
print "count_alpha is %d" % count_alpha
print "count_digit is %d" % count_digit
print "count_space is %d" % count_space
print "count_else is %d" % count_else
