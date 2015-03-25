from collections import *
from heapq import *
from bisect import *
from math import *
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input


n,t=mapper(mi, ri().split())
arr=mapper(mi, ri().split())
while t>0:
	t-=1
	i,j=mapper(mi, ri().split())
	m=inf
	for each in arr[i:j+1]:
		if each<m:
			m=each
	print m