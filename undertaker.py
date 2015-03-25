t=input()
while t>0:
	n=input()
	if "21" not in str(n) and n%21!=0:
		print "The streak lives still in our heart!"
	else:
		print "The streak is broken!"
	t-=1