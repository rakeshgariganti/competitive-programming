f=open("/home/rakesh/Desktop/python/O'Reilly - Python Cookbook.pdf","r").read().split(" ")
d={}
for i in f:
	if i in d:
		d[i] += 1
	else:
		d[i]=1

sorted(d)
print d