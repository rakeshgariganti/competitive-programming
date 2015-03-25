l=int(raw_input())
n=int(raw_input())
for i in xrange(n):
	w,h=map(int,raw_input().split(" "))
	if w<l or h<l:
		print "UPLOAD ANOTHER"
	elif w>=l and h>=l and w==h:
		print "ACCEPTED"
	elif w>=l or h>=l:
		print "CROP IT"
		