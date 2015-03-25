from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
inf=float('inf')

def lucky(n):
	for i in str(n):
		if i!="3" and i!="5":
			return False
	return True

if __name__=="__main__":
	tcase=int(raw_input())
	while tcase>0:
		tcase-=1
		n=int(raw_input())
		s=[int(i) for i in str(n)]
		carry=""
		for i in xrange(len(s)-1,-1,-1):
			if s[i]<4:
				s[i]=3
			elif s[i]==4:
				s[i]=5
			elif s[i]>=6:
				s[i]=3
				if i==0:
					carry="3"
				else:
					s[i-1]+=1
		tmp=""
		for i in s:
			tmp+=str(i)
		print lucky(carry+tmp),n,carry+tmp