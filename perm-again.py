from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
inf=float('inf')


if __name__=="__main__":

	dp=[0,1,1]
	for i in xrange(3,((10**5)+1)):
		dp.append(dp[-1]+i-1)
	tcase=int(raw_input())
	while tcase>0:
		tcase-=1
		n=int(raw_input())
		print dp[n]