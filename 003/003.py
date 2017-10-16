#!/usr/bin/python
# -*- coding: UTF-8 -*-
for m in range(0, 168):
	for n in range(0, 168):
		if (m + n)*(m - n) == 168:
			print "m:%d, n:%d" % (m, n)
			x = n*n - 100
			print "x:%d" % x 
print "no results!"
