t=input()
while t>0:
	s=raw_input().split(' ');
	l=len(s)
	for x in xrange(0,l/2):
		s[x],s[l-1-x]=s[l-1-x],s[x]
		print s[x],
	for i in s[l/2:]:
		print i,
	t-=1
