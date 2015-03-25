n=input()
li=map(int,raw_input().split(" "))
li1=[]
li2=[]
for x in li:
	if x%2==0:
		li1.append(x)
	else:
		li2.append(x)
li1.sort(reverse=False)	
li2.sort(reverse=True)
for i in li1:
	print i,
print 
for i in li2:
	print i,
