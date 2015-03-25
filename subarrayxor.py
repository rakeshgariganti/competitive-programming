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
	arr=mapper(mi, ri().split())
	me=[arr[0]]
	past=arr[0]
	for i in xrange(1,n):
		past^=arr[i]
		me.append(past)
	q=input()
	while q>0:
		q-=1
		a,b=mapper(mi, ri().split())
		if a==0:
			print me[b]
		else:
			print me[a]^me[b]