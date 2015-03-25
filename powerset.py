import itertools
t=input()
for x in xrange(t):
	c=0
	n=range(1,input()+1)
	for i in n:
		l=itertools.combinations(n,i)
		for k in l:
			for j in k:	
				c+=j
	print c