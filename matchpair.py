from collections import *
from heapq import *
from bisect import *
from math import *
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input

t=mi(ri())
while t>0:
	t-=1
	n=input()
	girls=mapper(mi,ri().split())
	boys=mapper(mi,ri().split())
	girls.sort()
	boys.sort(reverse=True)
	total=0
	for i in xrange(n):
		if girls[i]%boys[i]==0 or boys[i]%girls[i]==0:
			total+=1
	print total