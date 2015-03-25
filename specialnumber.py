from fractions import gcd
t=input()
def foo(n):
	ret=0
	for x in xrange(1,n+1):
		if gcd(n,x)==1:
			ret+=1
	return ret
while t>=1:
	n=input()
	ret=0
	for i in xrange(1,n+1):
		if n%i==0 :
			ret+=foo(i)
	print ret
	t-=1