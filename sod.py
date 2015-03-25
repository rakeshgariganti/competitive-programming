t=input()
s1=0
n2=0
def sodd(n):
	c=0
	while n>1:
		c=c+(n%10)
		n=n/10
	return c
for x in xrange(t):
	num=input()
	s1=s1+sodd(num)
	n2+=num
# print (s1%9)-(sodd(n2)%9)
print sodd(1123)