s=raw_input()
def pal(m):
	if m==m[::-1]:
		return True
	return False
total=set()
for i in xrange(len(s)):
	for j in xrange(len(s)):
		seed=s[i:j+1]
		if seed!="" and pal(seed):
			total.add((i,j+1))
print len(total)