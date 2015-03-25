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
	s5=n
	reached=False
	while s5>=0 and not reached:
		ts=n-s5
		if s5%3==0 and ts%5==0:
			reached=True
			break
		s5-=5
	if s5<0:
		print -1
	else:
		print '5'*s5+"3"*(n-s5)