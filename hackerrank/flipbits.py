# Enter your code here. Read input from STDIN. Print output to STDOUT
t=input()
while t>0:
    t-=1
    n=input()
    b=str(bin(n))[2:]
    f="0"*(32-len(b))+b
    s=[]
    for i in f:
    	if i=="0":
    		s.append("1")
    	else:
    		s.append("0")
    s=''.join(s)
    total=0
    for i in xrange(0,len(s)):
    	seed=s[len(s)-1-i]
    	if seed=="1":
    		total+=(2**i)
    print total