t=input()
for x in xrange(t):
	n=input()
	a=map(int, raw_input().split(" "))
	c=0
	for i in xrange(0,n-1):
		for j in xrange(i,n):
			temp=a[i] ^ a[j]
			if temp%2==1:
				c+=1
	print c