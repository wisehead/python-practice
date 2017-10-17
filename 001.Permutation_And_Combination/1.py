#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = {1, 2, 3, 4} 
for xxx in num:
	#print xxx,
	for xx in num:
		#print xx,
		for x in num:
			if x != xx and x != xxx and xx !=xxx:
				print xxx,xx,x
