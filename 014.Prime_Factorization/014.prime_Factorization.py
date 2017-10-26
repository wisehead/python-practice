#############################################################
#   File Name: 014.prime_Factorization.py
#     Autohor: Hui Chen (c) 2017
#        Mail: chenhui13@baidu.com
# Create Time: 2017/10/26-14:28:07
#############################################################
#!/usr/bin/env python 
#-*- coding:utf8 -*-
input_str = raw_input("please input n: ")
x = long(input_str)

n = x 
def prime_factor(level):
	global n 
	#print "level is %d" % level
	if n == x:
		print '{} ='.format(n),
	for k in range(2, n):
		#print "iteration :%d" % k 
		if n % k == 0:
			print '{} *'.format(k),
			n = n / k 
			prime_factor(level+1)
			break
		elif n - 1 == k:
			print '{}'.format(k+1)

prime_factor(1)
