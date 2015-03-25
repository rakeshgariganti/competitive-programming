tc=int(raw_input())
while tc>0:
	tc-=1
	num=raw_input()
	nums="2345679"
	s=1
	for i in num:
		if i in nums:
			print "NO"
			s=0
			break
	if s==1:
		if num==num[::-1]:
			print "YES"
		else:
			print "NO"