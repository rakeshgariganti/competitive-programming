# i loved working on this problem
# its me Rakesh

from collections import deque
n,p=map(int, raw_input().split(" "))
persons=[]
for x in xrange(n):
	if x>0:
		persons.append(-1)
	else:
		persons.append(0)
pairs=[]
for person in xrange(n):
	row=[]
	for each in xrange(n):
		row.append(False)
	pairs.append(row)
for y in xrange(p):
	f,s=map(int, raw_input().split(" "))
	pairs[f][s]=pairs[s][f]=True
q=deque()
q.append(0)
while len(q)>0:
	current=q.popleft()
	for i in xrange(n):
		if pairs[i][current] and persons[i]==-1:
			persons[i]=persons[current]+1
			q.append(i)
for i in xrange(1,n):
	print persons[i]