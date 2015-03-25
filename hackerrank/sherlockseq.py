from collections import deque
from collections import *
from heapq import *
from bisect import *
from math import *
mapper=map
makeint=int
makefloat=float
inf=makefloat('inf')
def getlist():
	return mapper(makeint, raw_input().split())
def getint():
	return makeint(raw_input())

dp={}
t=getint()
def sqr(a):
	if (int(sqrt(a))**2)==a:
		return True
	return False

while t>0:
	t-=1
	a,b=mapper(makeint, raw_input().split())
	start=0
	fsquare=0
	total=0
	for i in xrange(a,b+1):
		if sqr(i):
			start=i
			fsquare=int(sqrt(i))+1
			total+=1
			break
	
	if start==0:
		print 0
	else:
		start=fsquare**2
		fsquare+=1
		while start<=b:
			total+=1
			start=fsquare**2
			fsquare+=1
		print total