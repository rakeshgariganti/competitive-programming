from collections import deque
mapper=map
makeint=int
rawinput=raw_input
takeinput=input
t=takeinput()
while t>0:
	t-=1
	s=rawinput()
	slen=len(s)
	total=0
	last=s[0]
	for i in xrange(1,slen):
		if s[i]!=last:
			last=s[i]
			continue
		else:
			total+=1
	print total