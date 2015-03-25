from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
inf=float('inf')


if __name__=="__main__":
	tcase=int(raw_input())
	while tcase>0:
		tcase-=1
		a,b=map(int,raw_input().split())
		total=0
		for i in xrange(a,b+1):
			if str(i)==str(i)[::-1]:
				total+=1
		print total