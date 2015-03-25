from collections import deque
from collections import *
from heapq import *
from bisect import *
mapper=map
makeint=int
makefloat=float
inf=makefloat('inf')

t=int(raw_input())
while t>0:
	t-=1
	n,c,m=mapper(makeint, raw_input().split())
	total=0
	total+=(n/c)
	w=n/c
	last=0
	while w>=1:
		w+=last
		total+=(w/m)
		last=(w%m)
		w/=m
	print total