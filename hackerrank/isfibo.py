from collections import *
from heapq import *
from bisect import *
from math import *
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input

d={0:True,1:True}
a=0
b=1
t=mi(ri())
while t>0:
	t-=1
	n=mi(ri())
	if n<=b:
		if d.get(n,False):
			print "IsFibo"
		else:
			print "IsNotFibo"
	else:
		while b<=n:
			c=a+b
			a=b
			b=c
			d[c]=True
			if b==n:
				print "IsFibo"
				break
		if b!=n:
			print "IsNotFibo"