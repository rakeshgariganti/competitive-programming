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
	total=arr[0]
	for i in xrange(1,n):
		total^=arr[i]
	print total