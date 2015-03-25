#works for jus 60 marks

t=input()
while t>0:
	n=input()
	b,g=map(int, raw_input().split(" "))
	last="x"
	row=""
	for x in xrange(1,n+1):
		if b==0 or g==0:
			break
		if last=="x":
			if b<g:
				row+="g"
				g=g-1
				last="g"
			else:
				row+="b"
				b=b-1
				last="b"
		else:
			if x%2==0:
				if last=="b":
					g=g-1
					last="g"
					row+="g"
				else:
					b=b-1
					last="b"
					row+="b"
			else:
				if last=="g":
					g=g-1
					last="g"
					row+="g"
				else:
					b=b-1
					last="b"
					row+="b"
	if b==0:
		row+="g"*g
	if g==0:
		row+="b"*b
	te=jo=0
	for i in xrange(1,n):
		if row[i]==row[i-1]:
			jo+=1
		else:
			te+=1
	if jo>te:
		print "Little Jhool wins!"
	else:
		print "The teacher wins!"
	t-=1