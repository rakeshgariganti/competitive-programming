from collections import deque
mapper=map
makeint=int
rawinput=raw_input
takeinput=input
n,m=mapper(makeint,rawinput().split())
total=0
for i in xrange(m):
	a,b,c=mapper(makeint,rawinput().split())
	total+=((b-a+1)*c)
print total/n