#!/usr/bin/env python
#coding=utf-8
import random
ans=random.randint(1,99)
true=1
min=1
max=99
time=0
print "---�׷��K�X---"
while true:
	num=input("�q�@�Ʀr%d~%d:"%(min,max))
	if num>=max:
		print "��J�d�򤣲šA�Э��s��J!"
		continue
	if num<=min:
		print "��J�d�򤣲šA�Э��s��J!"
		continue
	if num>ans:
		max=num
	if num<ans:
		min=num
	if num==ans:
		true=0
	time=time+1
print "BOOM!!!�׷��K�X��%d�A�A�q�F%d��"%(ans,time)
print "\a"
		
