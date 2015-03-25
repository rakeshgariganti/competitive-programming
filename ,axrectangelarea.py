tc=int(raw_input())
while tc>0:
	tc-=1
	n=int(raw_input())
	s=n/4
	r=(n%4)/2
	print s*(s+r)