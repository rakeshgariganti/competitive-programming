
from fractions import gcd
n=input()
a=map(int, raw_input().split(" "))

for x in xrange(0,len(a)):
	for y in xrange(x+1,len(a)):
		if gcd(a[x], a[y])==1:
			a[x+1],a[y]=a[y],a[x+1]
			break
	print a[x],