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
	arr=mapper(mi, ri().split())
	total=0
	i=1
	start=arr[0]
	while i<n:
		tmptotal=0
		lastmax=i-1
		while i<n and arr[i]<start:
			tmptotal+=(start-arr[i])
			i+=1
		if i<n:
			total+=tmptotal
			start=arr[i]
			i+=1
		else:
			k=i-1
			back=arr[k]
			k-=1
			while k>=lastmax:
				tmpt=0
				while k>=lastmax and arr[k]<back:
					tmpt+=(back-arr[k])
					k-=1
				if k>=lastmax:
					total+=tmpt
					back=arr[k]
					k-=1
	print total%1000000007