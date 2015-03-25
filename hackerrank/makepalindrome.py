from collections import deque
mapper=map
makeint=int
rawinput=raw_input
takeinput=input
t=takeinput()
def change(a,b):
	c=0
	while a!=b:
		c+=1
		a=chr(ord(a)-1)

	return c

def cmp(left,right):
	if ord(left)>ord(right):
		return change(left,right)
	elif ord(left)<ord(right):
		return change(right,left)
	else:
		return 0
while t>0:
	t-=1
	s=rawinput()
	slen=len(s)
	total=0
	for i in xrange(0,slen/2):
		left=s[i]
		right=s[slen-1-i]
		total+=cmp(left, right)
	print total