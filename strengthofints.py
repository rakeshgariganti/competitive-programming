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
	n,m=mapper(mi, ri().split())
	set1=set(mapper(mi, ri().split()))
	set2=set(mapper(mi, ri().split()))
	print len(set1.intersection(set2))