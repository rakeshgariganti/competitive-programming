from collections import deque

def get(matrix,n,point):
	offsets=[(0,1),(0,-1),(1,0),(-1,0)]
	adj=[]
	for i in offsets:
		x,y=point[0]+i[0],point[1]+i[1]
		if x>=0 and x<n and y>=0 and y<n:
			if matrix[x][y]!="T":
				adj.append((x,y))
	return adj

def bfs(matrix,n,s,d):
	dp=[[-1]*n for i in xrange(n)]
	sx,sy=s[0],s[1]
	dp[sx][sy]=0
	q=deque()
	q.append(s)
	while len(q)>0:
		point=q.popleft()
		if point==d:
			break
		adjs=get(matrix, n, point)
		for adj in adjs:
			if dp[adj[0]][adj[1]]==-1:
				dp[adj[0]][adj[1]]=dp[point[0]][point[1]]+1
				q.append(adj)
			else:
				if dp[adj[0]][adj[1]]>dp[point[0]][point[1]]+1:
					dp[adj[0]][adj[1]]=dp[point[0]][point[1]]+1
	return dp[d[0]][d[1]]











n=input()
matrix=[]
s=(0,0)
d=(0,0)
for i in xrange(n):
	row=raw_input().split()
	for j in xrange(n):
		if row[j]=='S':
			s=(i,j)
		if row[j]=="E":
			d=(i,j)
	matrix.append(row)
print bfs(matrix,n,s,d)