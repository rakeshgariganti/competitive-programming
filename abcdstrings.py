import itertools
t=input()
while t>0:
	n,k=map(int, raw_input().split(" "))
	res=[]
	for x in xrange(k):
		res.append(raw_input())
	a=[]
	for roll in itertools.product(["a","b","c","d"], repeat = n):
		a.append("".join(roll))

	c=0
	for i in a:
		h=0
		for k in res:
			if k in i:
				h=1
		if h==0:
			c+=1
	print c
	t-=1