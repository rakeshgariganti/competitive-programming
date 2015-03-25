l=input()
r=input()
m=0
for i in xrange(l,r+1):
	for j in xrange(l,r+1):
		x= i^j
		if x>m:
			m=x
print m