#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
10000
10000 + 100000 * 7.5 /100 = 17500
17500 + 200000 * 5/100 = 27500
27500 + 200000 * 3/100 = 33500
33500 + 400000 * 1.5/100 = 39500
39500 + 
'''
str = raw_input("please input profit：");
I = long(str)
Salary = 0L
if I <= 100000:
	Salary = I * 0.1
	print "salary is: %ld" % Salary 
elif I < 200000:
	Salary = 10000 + (I - 100000) * 7.5 / 100
	print "salary is: %ld" % Salary 
elif I < 400000:
	Salary = 17500 + (I - 200000) * 5 / 100
	print "salary is: %ld" % Salary 
elif I < 600000:
	Salary = 27500 + (I - 400000) * 3 / 100
	print "salary is: %ld" % Salary 
elif I < 1000000:
	Salary = 33500 + (I - 600000) * 1.5 / 100
	print "salary is: %ld" % Salary 
else:
	Salary = 39500 + (I - 1000000) * 1 / 100
	print "salary is: %ld" % Salary 
