from collections import deque
from collections import *
from heapq import *
from bisect import *
mapper=map
makeint=int
makefloat=float
inf=makefloat('inf')
def getlist():
	return mapper(makeint, raw_input().split())
def getint():
	return makeint(raw_input())

t=getint()
while t>0:
	t-=1
	