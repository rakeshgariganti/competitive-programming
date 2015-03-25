tc=input()
while tc>0:
	tc-=1
	z,n=map(int, raw_input().split())
	arr=map(int, raw_input().split())
	me=z
	for i in arr:
		me=(me&i)
		if me==0:
			break
	if me==0:
		print "Yes"
	else:
		print "No"
