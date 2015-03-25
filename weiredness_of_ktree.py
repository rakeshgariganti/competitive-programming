t= input()
for x in xrange(t):
	k,m=map(int,raw_input().split(" "))
	l=k**m
	nodes=((k**(m+1))-1)/(k-1)
	w=0
	while nodes>0:
		w=w+(nodes%10)
		nodes=nodes/10
	print w