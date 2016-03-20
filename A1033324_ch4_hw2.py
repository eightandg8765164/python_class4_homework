#!/usr/bin/env python
#coding=utf-8
import random
ans=random.randint(1,99)
true=1
min=1
max=99
time=0
print "---終極密碼---"
while true:
	num=input("猜一數字%d~%d:"%(min,max))
	if num>=max:
		print "輸入範圍不符，請重新輸入!"
		continue
	if num<=min:
		print "輸入範圍不符，請重新輸入!"
		continue
	if num>ans:
		max=num
	if num<ans:
		min=num
	if num==ans:
		true=0
	time=time+1
print "BOOM!!!終極密碼為%d，你猜了%d次"%(ans,time)
print "\a"
		
