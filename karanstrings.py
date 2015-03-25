tc=int(raw_input())
while tc>0:
	tc-=1
	s=raw_input()
	i=0
	slen=len(s)
	final=""
	while i<slen:
		c=s[i]
		final+=c
		while i<slen and s[i]==c:
			i+=1
	print final