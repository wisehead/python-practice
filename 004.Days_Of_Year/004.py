#############################################################
#   File Name: 004.py
#     Autohor: Hui Chen (c) 2017
#        Mail: chenhui13@baidu.com
# Create Time: 2017/10/17-10:53:12
#############################################################
#!/usr/bin/env python 
#-*- coding:utf8 -*-
days_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days_array = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap_year(year ):
    if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return 1
			else:
				return 0
		else:
			return 1
    else:
		return 0 

input_str = raw_input("please input year: ")
year = long(input_str)
input_str = raw_input("please input month: ")
month = long(input_str)
input_str = raw_input("please input day: ")
day = long(input_str)
days_of_year = 0
for i in range(0, month - 1):
	days_of_year += days_array[i]
days_of_year += day
if is_leap_year(year):
	days_of_year += 1
print "Days of Year: %d" % days_of_year
