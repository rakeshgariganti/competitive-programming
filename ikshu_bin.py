def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
k,n=map(int, raw_input().split(" "))
s="1"*n
k=2**k
c=0
for x in xrange(k):
	hmm=str(bin(x))
	if s in hmm:
		c+=1
g=gcd(c, k)
print str(c/g)+"/"+str(k/g)