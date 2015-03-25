from collections import *
from heapq import *
from bisect import *
from math import *
from time import sleep
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
	arr.sort()
	total=0
	start=0
	while start<n:
		val=arr[start]
		this=start
		while start<n and arr[start]==val:
			start+=1
		calc=start-this
		total+=(calc*(calc-1))
	print total
