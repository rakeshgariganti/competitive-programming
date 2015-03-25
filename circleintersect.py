from collections import deque
import math
mapper=map
makeint=int
makefloat=float
rawinput=raw_input
takeinput=input
t=takeinput()
while t>0:
	t-=1
	vals=mapper(makeint, rawinput().split())
	x1=vals[1]
	y1=vals[2]
	x2=vals[3]
	y2=vals[4]
	r1=min(mapper(makefloat,rawinput().split()))
	r2=min(mapper(makefloat,rawinput().split()))
	d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	if d>=r1+r2:
		print("%.2f" % 0)
	elif d<abs(r1-r2):
		m=min(r1,r2)
		print("%.2f" % (math.pi*m*m))
	else:
		alpha=math.acos((r1*r1+d*d-r2*r2)/(2*r1*d))
		beta=math.acos((r2*r2+d*d-r1*r1)/(2*r2*d))
		area=r1*r1*(alpha-(0.5*math.sin(2*alpha)))+r2*r2*(beta-(0.5*math.sin(2*beta)))
		print("%.2f", area)