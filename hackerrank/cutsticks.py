n=int(raw_input())
sticks=map(int, raw_input().split())
total=0
sticks.sort()
m=0
while m<n:
	now=sticks[m]
	ok=m+1
	while ok<n and sticks[ok]==now:
		ok+=1
	print n-m
	m=ok