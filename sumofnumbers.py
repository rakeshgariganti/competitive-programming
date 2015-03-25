from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input


t=mi(ri())
while t>0:
	t-=1
	n=input()
	arr=mapper(mi, ri().split())
	s=input()
	yes=False
	for i in xrange(0,n+1):
		if yes:
			break
		for j in combinations(arr,i):
			if sum(j)==s:
				yes=True
				break
	if yes:
		print "YES"
	else:
		print "NO"