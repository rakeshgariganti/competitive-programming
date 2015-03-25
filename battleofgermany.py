t=input()
def area(x1,y1,x2,y2,x3,y3):
	a=x1*(y2-y3)
	a=a+(x2*(y3-y1))
	a=a+(x3*(y2-y3))
	return abs(a/2)

while t>0:
	x1,y1,x2,y2,x3,y3,x,y=map(float,raw_input().split(" "))
	o=area(x1,y1,x2, y2, x3, y3)
	i=(area(x, y, x2, y2, x3, y3)+area(x, y, x1, y1, x3, y3)+area(x, y, x2, y2, x1, y1))
	if o==i:
		print "INSIDE"
	else:
		print "OUTSIDE"
	t-=1