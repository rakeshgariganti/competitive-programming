k=int(raw_input())
p=map(int,raw_input().split())
p.sort(reverse=True)
print max(i+p[i]+2 for i in xrange(k))
