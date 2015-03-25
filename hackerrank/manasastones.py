# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
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
	n=mi(ri())
	a=mi(ri())
	b=mi(ri())
	x=min(a,b)
	y=max(a,b)
	if x==y:
		hi=0
		for i in xrange(1,n):
			hi+=x
		print hi
	else:
		for i in xrange(n):
			print i*y+((n-1-i)*x),
		print 