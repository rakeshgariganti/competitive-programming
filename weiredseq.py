n=input()
seq=map(int, raw_input().split(" "))
globm=[]
maxlen=1
p=seq[0]
q=None
for i in xrange(1,len(seq)):
	calc=0
	if q==None:
		q=((seq[i]-p)/(-1**(i+2)))
		p=seq[i]
		maxlen+=1
	else:
		calc=p+(q*((-1)**(i+2)))
		if seq[i]==calc:
			p=calc
			maxlen+=1
		else:
			globm.append(maxlen)
			maxlen=1
			q=None
if len(globm)>0:
	print max(globm)
else:
	print maxlen