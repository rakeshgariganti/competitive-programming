t=input()
def check(asd):
	print asd
	li=[]
	for i in asd:
		if i!=":":
			if i in li:
				return False
			else:
				li.append(i)
def make(h,m,s):
	return str(h)+":"+str(m)+":"+str(s)
for x in xrange(t):
	ti=raw_input()

	while check(ti)==False:
		h,m,s=ti.split(":")
		s=str(int(s)+1)
		if int(s)>=60:
			s="0"
			m=str(int(m)+1)
			if int(m)>=60:
				m="0"
				h=str(int(h)+1)
				if int(h)>=24:
					h="0"
		if int(s)<10:
			s="0"+s
		if int(m)<10:
			m="0"+m
		if int(h)<10:
			h="0"+h
		ti=make(h,m,s)
	print ti