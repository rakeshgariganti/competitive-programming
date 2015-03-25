t=input()
for i in xrange(t):
	pos,n=map(int, raw_input().split(" "))
	for x in xrange(n):
		if pos==0:
			pos=1
		elif pos==2:
			pos=1
		else:
			pos=0
	print pos