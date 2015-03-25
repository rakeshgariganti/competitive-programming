n=input()
arr=map(int, raw_input().split())
c={}
for i in arr:
	if i in c:
		c[i]+=1
	else:
		c[i]=1
for i in range(100):
	if i in c:
		print c[i],
	else:
		print 0,