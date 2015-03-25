from collections import deque
mapper=map
makeint=int
rawinput=raw_input
takeinput=input
n,m=mapper(makeint, rawinput().split(' '))
topics=[]
for i in xrange(n):
	c=0
	s=raw_input()
	top=set()
	for j in xrange(m):
		if s[j]=="1":
			top.add(j)
	topics.append(top)
maxtopics=0
maxteams=0
for i in xrange(n):
	for j in xrange(i+1,n):
		ttop=len(topics[i]|topics[j])
		if ttop>maxtopics:
			maxtopics=ttop
			maxteams=1
		elif ttop==maxtopics:
			maxteams+=1
print maxtopics
print maxteams