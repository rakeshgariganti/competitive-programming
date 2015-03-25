t=input()
while t>0:
	size=input()
	matrix=[]
	pos=None
	for x in xrange(size):
		row=raw_input()
		matrix.append(row)
	h=True
	v=True
	for each in xrange(0,size/2):
		if matrix[each]!=matrix[size-each-1]:
			h=False
		for col in xrange(0,size/2):
			if matrix[each][col]!=matrix[each][size-col-1]:
				v=False
	
		
	if v and h:
		print "BOTH"
	elif v:
		print "VERTICAL"
	elif h:
		print "HORIZONTAL"
	else:
		print "NO"
	t-=1