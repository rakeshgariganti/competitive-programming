tc=input()
while tc>0:
	tc-=1
	s=raw_input().split('*')
	total=0
	for i in s:
		there= False
		for j in i:
			if j!="O":
				there=True
				break
		if not there:
			total+=len(i)
	print total