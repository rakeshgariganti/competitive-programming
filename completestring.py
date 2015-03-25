t=input()
while t>0:
	t-=1
	s=raw_input()
	alpha=[]
	for i in range(97,97+26):
		alpha.append(chr(i))
	for i in s:
		if len(alpha)>0:
			if i in alpha:
				alpha.remove(i)
		else:
			break
	if len(alpha)>0:
		print "NO"
	else:
		print "YES"