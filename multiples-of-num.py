from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
inf=float('inf')


if __name__=="__main__":
	t=int(raw_input())
	while t>0:
		t-=1
		total=0
		a,b,m=map(int,raw_input().split())
		
		total+=(b/m)-((a-1)/m)
		print total
