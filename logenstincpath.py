from collections import deque
mapper=map
makeint=int
rawinput=raw_input
takeinput=input
t=takeinput()
def rakz(mat,r,c,me):
	
while t>0:
	t-=1
	m,n=mapper(makeint,rawinput().split())
	matrix=[]
	while n>0:
		matrix.append(mapper(makeint,rawinput().split()))
		n-=1
