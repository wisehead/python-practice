#!/usr/bin/env python 
#-*- coding:utf8 -*-
'''
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''
listA0 = ['c','a','b']
listB0 = ['x','y','z']
listA = listA0[:]
listB = listB0[:]
for i in listA:
	for j in listB:
		if i=='a' and j=='x':
			pass
		if i=='c' and j=='x':
			pass
		if i=='a' and j=='z':
			pass
		print " %c:%c" % (i,j)
		listB.remove(j)
		#break
