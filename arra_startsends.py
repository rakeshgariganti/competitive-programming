t=input()
for i in xrange(t):
	n=input()
	l1={}
	l2={}
	array=map(int, raw_input().split())
	for k in xrange(0,n):
		item=array[k]
		if item not in l1:
			l1[item]=k
		else:
			l2[item]=k
	m=0
	for i in l1:
		if i in l2:
			if l2[i]-l1[i]>m:
				m=l2[i]-l1[i]
	print m+1
