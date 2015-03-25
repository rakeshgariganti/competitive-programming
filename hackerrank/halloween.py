from collections import deque
from collections import *
from heapq import *
from bisect import *
from math import *
mapper=map
makeint=int
makefloat=float
inf=makefloat('inf')


t=makeint(raw_input())
while t>0:
	t-=1
	k=makeint(raw_input())
	a=b=0
	if k%2==0:
		a=b=(k/2)
	else:
		a=k/2
		b=a+1
	print a*b