from collections import deque
mapper=map
makeint=int
rawinput=raw_input
takeinput=input
t=takeinput()
while t>0:
	t-=1
	a,b=mapper(makeint, rawinput().split(" "))
	me=0
	routes=[]
	for x in xrange(1001):
		row=[]
		for y in xrange(1001):
			row.append(False)
		routes.append(row)
	for x in xrange(b):
		m,n=mapper(makeint, rawinput().split(" "))
		routes[m][n]=routes[n][m]=True
	q=deque()
	q.append(1)
	visited=[]
	while len(q)>0:
		current=q.popleft()
		me+=1
		if me>=a:
			break
		for x in xrange(1,b+1):
			if x not in visited:
				if routes[current][x]:
					q.append(x)
		visited.append(current)
	print me-1


# Actual solution
# tc = int(raw_input())
# while (tc>0):
# 	tc = tc - 1
# 	a, b = map(int, raw_input().split())
# 	while (b>0):
# 		b = b - 1
# 		m, n = map(int, raw_input().split())
# 	print a-1