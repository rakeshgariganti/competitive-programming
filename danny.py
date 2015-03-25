n=input()
s=set()
def rev(p):
	pr=""
	for i in xrange(len(p)-1,-1,-1):
		pr=pr+p[i]
	return pr
for i in xrange(n):
	pas=raw_input()
	if rev(pas) in s:
		print str(len(pas))+" "+pas[(len(pas)/2)]
		break
	s.add(pas)