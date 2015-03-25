t=int(raw_input())
while t>0:
	t-=1
	n=int(raw_input())
	li=map(int, raw_input().split())
	if n==1:
		print "YES"
		continue
	if n==2:
		print "NO"
		continue

	s=sum(li)
	left=li[0]
	done=False
	for i in xrange(1,n-1):
		right=s-left-li[i]
		if left==right:
			print "YES"
			done=True
			break
		left=left+li[i]
	if not done:
		print "NO"