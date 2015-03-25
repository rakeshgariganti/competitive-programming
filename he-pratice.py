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

if __name__=="__main__":
	t=mi(ri())
	fact={1:1}
	for i in xrange(2,101):
		fact[i]=fact[i-1]*i
	while t>0:
		t-=1
		n=input()
		print fact[n]
		