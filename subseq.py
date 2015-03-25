
def ctoi(c):
	if c>='a':
		return ord(c)-ord('a')
	elif c>='A':
		return ord(c)-ord('A')+26
	else:
		return 52+int(c)+1

def solve(s,qster):
	qchars=[False]*62
	qlen=0
	for i in qster:
		qlen+=1
		qchars[ctoi(i)]=True
	n=len(s)
	total=False
	ans=0
	print "qlen:"+str(qlen)
	for x in xrange(0,n):
		print "Starting at:"+s[x]
		done=0
		nxt=x+qlen-1
		for i in xrange(nxt,n):
			print "to:"+s[i]
			if qchars[ctoi(s[i])]:
				done+=1
			print "dones:"+str(done)+" at:"+str(i)
			if done==qlen:
				if not total:
					ans+=(n-i)+x
					total=True
				else:
					print "me"
					ans+=(n-i)+x-1
				print "ans:"+str(ans)
				break
			
	print ans
t=input()
while t>0:
	t-=1
	s=raw_input()
	q=input()
	while q>0:
		q-=1
		qster=raw_input()
		print "s:"+s+"  q:"+qster
		solve(s,qster)