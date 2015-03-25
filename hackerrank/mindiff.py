n = input()
k = input()
candies = [input() for _ in xrange(0,n)]
candies.sort()
min_diff =candies[-1] ## Write code here to compute the answer using (n, k, candies)
for i in xrange(0,n-k+1):
	calc=candies[i+k-1]-candies[i]
	if calc<min_diff:
		min_diff=calc
print min_diff
