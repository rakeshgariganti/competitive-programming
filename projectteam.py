from collections import deque
mapper=map
makeint=int
rawinput=raw_input
takeinput=input
t=takeinput()
while t>0:
	t-=1
	stu=mapper(makeint, rawinput().split())
	n=stu[0]
	stu=stu[1:]
	stu.sort()
	myl=[]
	for i in xrange(0,n/2):
		myl.append(stu[i]+stu[n-1-i])
	myl.sort()
	print abs(myl[0]-myl[-1])