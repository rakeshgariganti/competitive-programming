t=input()
while t>0:
	n=input()
	cars=map(int, raw_input().split())
	a=1
	for i in xrange(1,n):
		if cars[i-1]>=cars[i]:
			a=a+1
	print a
	t-=1