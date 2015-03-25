n=input()
band=raw_input()
d=[]
i=0
while i<len(band):
	s=[]
	tmp=""
	while band[i]=="w" or band[i]==tmp or tmp=="w" or tmp=="":
		if band[i]!="w":
			tmp=band[i]
		s.append(band[i])
		i+=1
		if i>=len(band):
			break
	d.append(s)

for x in xrange(0,len(d)-1):
	if d[x][-1]=="w":
		i=-1
		while d[x][i]=="w":
			i-=1
		if len(d[x])<len(d[x+1]):
			d[x+1].extend(d[x][:i:-1])
			while i<-1:
				d[x].pop(i+1)
				i+=1
m=0
def which(l):
	for i in l:
		if i=="r" or i=="b":
			return i
for x in xrange(0,len(d)-1):
	tmplen=len(d[x])+len(d[x+1])
	if x==len(d)-2:
		if which(d[x+1])==which(d[0]):
			tmplen+=len(d[0])
	if x==0:
		if which(d[0])==which(d[-1]):
			tmplen+=len(d[-1])
	if tmplen>m:
		m=tmplen
z=len(d[0])+len(d[-1])

if m>z:
	print m
else:
	print z