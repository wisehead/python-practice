#!/usr/bin/env python 
#-*- coding:utf8 -*-
'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
'''
magic_num = 2
input_str = raw_input("please input add_count:")
add_count = long(input_str)
input_str = raw_input("please input magic_num:")
magic_num = long(input_str)
num_list = [] 
sum_total = long(0)
for i in range (0,add_count):
	if i== 0:
		num_list.append(magic_num)
		pass
	else:
		num_list.append(num_list[i-1]*10 + magic_num)

for num in num_list:
	sum_total += num
	print num
print sum_total
