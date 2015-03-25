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

	s=ri()
	slen=len(s)
	t=mi(ri())
	while t>0:
		t-=1
		a,b=mapper(mi, ri().split())
		if a>=slen:
			a=a%slen
		if b>=slen:
			b=b%slen
		if s[a-1]==s[b-1]:
			print "Yes"
		else:
			print "No"