t=input()
while t>0:
	a,b=map(int, raw_input().split(" "))
	m=-1
	for i in xrange(a,b+1):
		for k in xrange(i+1,b+1):
			an=i&k
			if an>m:
				m=an
	print m
	t-=1