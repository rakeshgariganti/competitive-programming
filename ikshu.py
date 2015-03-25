s=input()
k=map(int, raw_input().split(" "))
c=0
k.sort()
for x in k:
	print x-c,
	c+=1