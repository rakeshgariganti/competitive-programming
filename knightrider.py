d={}
size=5
path=[]
visited=[]

def cordToId(x,y):
	return (x)*size+y
def validCord(x):
	if x>=0 and x<size:
		return True
	return False
def getValidMoves(x,y):
	moves=[]
	offsets=[(-1,-2),(-2,-1),(1,-2),(-2,1),(-1,2),(2,-1),(1,2),(2,1)]
	for i in offsets:
		m=x+i[0]
		n=y+i[1]
		if validCord(m) and validCord(n):
			moves.append((m,n))
	return moves
for x in xrange(0,size):
	for y in xrange(0,size):
		d[cordToId(x,y)]=[]
		moves=getValidMoves(x,y)
		for i in moves:
			to=cordToId(i[0],i[1])
			d[cordToId(x,y)].append(to)
def orderByAvail(n):
    resList = []
    for v in d[n]:
        if v not in visited:
            c = 0
            for w in d[v]:
                if w not in visited:
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


def ride(n,path,u,limit):
	visited.append(u)
	path.append(u)
	if n<limit:
		ads=orderByAvail(u)
		i=0
		done=False
		while i<len(ads) and not done:
			if ads[i] not in visited:
				done=ride(n+1, path, ads[i], limit)
			i+=1
		if not done:
			path.pop()
			visited.pop()
	else:
		done=True
		print len(path)
	return done
g={
	'a':['b','d'],
	'b':['c','d'],
	'c':[],
	'd':['e'],
	'e':['b','f'],
	'f':['c']
}
s=ride(1, path,0,(size**2))
print path
print "starting at: "+str(0)+" "+str(s)