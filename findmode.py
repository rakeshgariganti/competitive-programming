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
	d={}
	m=0
	for i in arr:
		try:
			d[i]+=1
			if d[i]>m:
				m=d[i]
		except KeyError:
			d[i]=1
	maar=[]
	for i in d:
		if d[i]==m:
			maar.append(i)
	maar.sort(reverse=True)
	for i in maar:
		print i,
	print