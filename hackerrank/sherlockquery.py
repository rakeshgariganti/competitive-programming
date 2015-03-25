n,m=map(int, raw_input().split())
aa=[0]
ba=[0]
ca=[0]
aa.extend(map(int, raw_input().split()))
ba.extend(map(int, raw_input().split()))
ca.extend(map(int, raw_input().split()))
for i in xrange(1,m+1):
	c=ca[i]
	seed=ba[i]
	while seed<=n:
		aa[seed]=(aa[seed]*c)%1000000007
		seed+=ba[i]
for i in xrange(1,n+1):
	print aa[i]%1000000007,