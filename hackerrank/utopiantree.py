from collections import deque
mapper=map
makeint=int
rawinput=raw_input
takeinput=input
t=takeinput()
while t>0:
	t-=1
	n=input()
	total=1
	for i in xrange(1,n+1):
		if i%2==1:
			total*=2
		else:
			total+=1
	print total
