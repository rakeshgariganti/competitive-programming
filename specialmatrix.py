t=input()
while t>0:
	size=input()
	matrix=[]
	pos=None
	for x in xrange(size):
		row=raw_input()
		for i in xrange(0,size):
			if row[i]=="*":
				pos=(x+1,i+1)
	s=(size/2)+1
	print abs(s-pos[0])+abs(s-pos[1])
	t-=1