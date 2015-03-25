t=input()
def findway(lines,before,s,d):
	reached=False
	length=0
	stop=d
	path=before
	path.append(s)
	while reached==False:
			start=path[-1]
			there=False
			mindest=-1
			mindist=-1
			p=-1
			for each in lines:
				if reached ==True:
					break
				if start==each[0]:
					p=each[1]
				elif start==each[1]:
					p=each[0]
				else:
					p=-1
				if p != -1 and p not in path:
					there=True
					if p==stop:
							reached=True
							length+=each[2]
							path.append(stop)
					else:
						if mindist==-1:
							mindist=each[2]
							mindest=p
						else:
							if each[2]<mindist:
								mindist=each[2]
								mindest=p
			if there==True and reached==False:
				length+=mindist
				path.append(mindest)
			if there==False and reached==False:
				break
	if reached==True:
		return path,length
	else:
		return path,-1



for test in xrange(t):
	lines=[]
	n,k=map(int,raw_input().split(" "))
	for line in xrange(k):
		sourse,dest,distance=map(int, raw_input().split(" "))
		lines.append((sourse,dest,distance))
	mys,via,myd=map(int, raw_input().split(" "))
	p1,l1=findway(lines,[],mys, via)
	if l1!=-1:
		p2,l2=findway(lines,p1[:-1],via, myd)
		if l2==-1:
			print "No Train Found."
		else:
			print l1+l2
			for i in p2:
				print i,
	else:
		print "No Train Found."