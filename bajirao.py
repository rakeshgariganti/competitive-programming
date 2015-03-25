n=int(raw_input())
for i in xrange(n):
	s=raw_input()
	yes=1
	for k in xrange(0,len(s)-1):
		print s[k]
		if s[k]==s[k+1]:
			print "SLAP"
			yes=0
			break
	if yes==1:
		print "KISS"