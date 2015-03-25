n=input()
if n>0:
	arr=map(int, raw_input().split())
	s=arr[0]
	m=s
	for i in xrange(1,n):
		s=s+arr[i]
		if s<=0:
			s=0
		else:
			if s>m:
				m=s
	print m
else:
	print 0