n=size=int(raw_input())
mat=[]
while n>0:
	n-=1
	l=raw_input()
	row=[]
	for i in l:
		row.append(int(i))
	mat.append(row)

for i in xrange(1,size-1):
	for j in xrange(1,size-1):
		c=mat[i][j]
		if mat[i-1][j]<c and mat[i][j-1]<c and mat[i][j+1]<c and mat[i+1][j]<c:
			mat[i][j]='X'

for i in mat:
	row=''
	for j in i:
		row+=str(j)
	print row