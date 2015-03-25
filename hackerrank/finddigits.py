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
	n=ri()
	num=int(n)
	total=0
	for i in n:
		if i!="0":
			if num%int(i)==0:
				total+=1
	print total