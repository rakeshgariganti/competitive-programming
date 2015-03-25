n,m=map(int, raw_input().split())
mp=dict()
for i in xrange(n):
	row=map(int, raw_input().split())
	for j in xrange(m):
		mp[row[j]]=(i,j)
q=input()
for k in xrange(q):
	query=int(raw_input())
	x,y=mp.get(query,(-1,-1))
	print x,y