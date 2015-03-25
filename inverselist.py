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
m=0
while m<t:
	m+=1
	print m
	n=input()
	li=mapper(mi, ri().split())
	no=True
	for i in li:
		try:
			if li[i-1]!=i:
				no=False
		except:
			no=False
	print li
	if no:
		print "inverse"
	else:
		print "not inverse"